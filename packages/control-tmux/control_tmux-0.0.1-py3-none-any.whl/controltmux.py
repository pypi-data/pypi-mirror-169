#!/usr/bin/python3

#
# control-tmux: Wrapper script around tmux that enables quickly switching between
# sessions, history saving and loading.
#
# Copyright 2018 Katie Rust (https://ktpanda.org)
#
# Redistribution and use in source and binary forms, with or without modification, are
# permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this list of
# conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice, this list
# of conditions and the following disclaimer in the documentation and/or other materials
# provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY
# EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL
# THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
# STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF
# THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

import sys
import re
import tempfile
import time
import traceback
import stat

import os
import fcntl
import termios
import array
import select
import subprocess
import signal
import errno
from collections import deque, defaultdict
from pathlib import Path
from os.path import basename, exists, join, getsize, isdir, getmtime
from argparse import ArgumentParser
import zipfile

VERSION = "0.0.1"

TMUX = '/usr/local/bin/tmux'
if not exists(TMUX):
    TMUX = '/usr/bin/tmux'

RETRY_ERRNO = errno.EAGAIN, errno.EINTR

tmux_sock = None

tmuxenv = dict(os.environ)
tmuxenv.pop('TMUX', None)

def runproc(args, capture=False, **kw):
    if capture:
        return subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=tmuxenv, encoding='utf8', errors='ignore', **kw)
    else:
        return subprocess.run(args, **kw)

def get_ssh_sock(host):
    return Path.home() / '.ssh' / (f'control-{host}')

def tmux(lst, capture=True, host=None, **kw):
    if host:
        args = ['ssh', '-S', get_ssh_sock(host), '', ('-T' if capture else '-t'), escape_shell(['tmux'] + lst)]
    else:
        args = [TMUX, '-S', tmux_sock] + lst
    p = runproc(args, capture, **kw)
    return p.stdout, p.returncode

try:
    del os.environ['debian_chroot']
except KeyError:
    pass

SAVEDIR = '%s/.tmuxsave' % os.getenv('HOME')

class TmuxControl:
    def __init__(self, sock, savedir, debug=False, notify_pipe=None):
        self.sock = sock
        self.savedir = savedir
        self.debug = debug
        self.notify_pipe = notify_pipe

        self.old_sessions = {}
        self.old_panes = set()

        self.command_callback = deque([((lambda lines: None), (), {})])
        self.cur_lines = None
        self.instance = None
        self.instance_dir = None
        self.list_command_outstanding = False

        sub_env = dict(os.environ)
        sub_env.pop('TMUX', None)
        tmux_args = ['tmux', '-C', '-S', sock, 'new-session', '-A', '-D', '-s', '_control', 'cat']

        self.proc = subprocess.Popen(tmux_args, env=sub_env, stdin=subprocess.PIPE, stdout=subprocess.PIPE)

        self.command('show-env -g TMUX_INSTANCE', self.get_instance_callback)
        self.do_session_log()

    def read_command_output(self):
        while True:
            r = self.proc.stdout.readline()
            if not r:
                break

            r = r.decode('utf-8', 'ignore').rstrip('\n')
            if r.startswith('%'):
                lst = r.split()
                event = lst[0]
                func = getattr(self, 'evt_%s' % event[1:].replace('-', '_'), None)
                if func:
                    func(lst)
                else:
                    if self.debug:
                        print('unhandled event: %s' % r)
            elif self.cur_lines is not None:
                self.cur_lines.append(r)

    def command(self, cmd, cb, *a, **kw):
        self.command_callback.append((cb, a, kw))
        self.proc.stdin.write((cmd + '\n').encode('utf-8'))
        self.proc.stdin.flush()

    def evt_begin(self, argv):
        self.cur_lines = []

    def evt_end(self, argv):
        lines = self.cur_lines
        self.cur_lines = None
        f, a, kw = self.command_callback.popleft()
        return f(lines, *a, **kw)

    evt_error = evt_end

    def evt_sessions_changed(self, argv):
        if self.debug:
            print('session change event: %s' % argv[0])
        if not self.list_command_outstanding:
            self.do_session_log()

    evt_session_renamed = evt_sessions_changed
    evt_window_add = evt_sessions_changed
    evt_window_close = evt_sessions_changed
    evt_unlinked_window_add = evt_sessions_changed
    evt_unlinked_window_close = evt_sessions_changed
    evt_linked_window_add = evt_sessions_changed
    evt_linked_window_close = evt_sessions_changed

    def do_session_log(self):
        #self.list_command_outstanding = True
        self.command('list-panes -a -F "#{session_name}|#{window_index}.#{pane_index}|#{pane_id}"', self.list_session_callback)

    def list_session_callback(self, lines):
        sessions = defaultdict(list)
        allpanes = set()
        #self.list_command_outstanding = False
        for l in lines:
            sid, win, pane = l.split('|')
            pane = pane.lstrip('%')
            if sid != '_control':
                sessions[sid].append('%s=%s' % (win, pane))
                allpanes.add(pane)

        if self.debug:
            print('sessions:')

        for sess, panes in sessions.items():
            old_panes = self.old_sessions.get(sess)
            if panes == old_panes:
                continue
            txt = '%s %s' % (sess, ' '.join(panes))
            if self.debug:
                print(txt)
            for sessfn in (join(self.savedir, '%s.session' % sess), join(self.instance_dir, '%s.session' % sess)):
                with open(sessfn, 'w') as fp:
                    fp.write('%s\n%s\n' % (self.instance, txt))


        deleted_sessions = self.old_sessions.keys() - sessions.keys()

        for sess in deleted_sessions:
            if self.debug:
                print('deleted session %s' % sess)
            for sessfn in (join(self.savedir, '%s.session' % sess), join(self.instance_dir, '%s.session' % sess)):
                try:
                    os.rename(sessfn, sessfn + '-obs')
                except EnvironmentError:
                    pass

        deleted_panes = self.old_panes - allpanes
        for pane in deleted_panes:
            if self.debug:
                print('deleted pane %s' % pane)
            for suffix in ('-hist', '-pwd'):
                try:
                    fn = join(self.instance_dir, pane + suffix)
                    os.rename(fn, join(self.instance_dir, 'obs-%s%s' % (pane, suffix)))
                except EnvironmentError:
                    pass

        if self.debug:
            print()

        self.old_panes = allpanes
        self.old_sessions = sessions

    def get_instance_callback(self, lines):
        if self.debug:
            print(lines)
        env = dict(lin.split('=', 1) for lin in lines if '=' in lin)
        instance = env.get('TMUX_INSTANCE')
        if instance is None:
            sock_time = int(getmtime(self.sock))
            sock_time_str = time.strftime('%Y-%m-%d__%H-%M-%S', time.localtime(sock_time))
            instance = '%s-%s' % (basename(self.sock), sock_time_str)
            self.command('setenv -g TMUX_INSTANCE "%s"' % instance, lambda lines: None)
            if self.debug:
                print('set instance to %s' % instance)
        self.instance = instance
        self.instance_dir = join(self.savedir, 'tmux-' + instance)
        try:
            os.makedirs(self.instance_dir)
        except OSError:
            pass
        if self.debug:
            print('instance=%s' % instance)
        if self.notify_pipe is not None:
            os.close(self.notify_pipe)
            self.notify_pipe = None


class TmuxQuery:
    ivars = ()
    vars = ()
    args = []
    def __init__(self, **kw):
        for k, v in kw.items():
            setattr(self, k, v)

    @classmethod
    def run(cls, args=[], xargs=[], host=None):
        # Need a unique separator. We used to use an ASCII control
        # character, but newer versions of TMUX filter those out.
        # Also filters any non-ASCII characters 🤬  (╯°□°)╯︵ ┻━┻
        sep = f'<d-_-b>'
        allvars = cls.ivars + cls.vars
        out, ex = tmux(args + cls.args + xargs + ['-F', sep.join('#{%s}' % v for v in allvars)], host=host)
        r = []
        for line in out.splitlines():
            self = cls()
            i = iter(line.split(sep, len(allvars) - 1))
            for k in cls.ivars:
                setattr(self, k, int(next(i)))
            for k in cls.vars:
                setattr(self, k, next(i))
            r.append(self)
        return r

    def __repr__(self):
        return '%s(%s)' % (type(self).__name__, ', '.join('%s=%r' % (k, getattr(self, k, None)) for k in (self.ivars + self.vars)))

class ListSessions(TmuxQuery):
    args = ['list-sessions']
    ivars = ('session_windows', 'session_attached')
    vars = ('session_created_string', 'session_name')

class Pane(TmuxQuery):
    ivars = 'window_index', 'line', 'pane_pid'
    vars = 'pane_id', 'session_name'
    args = ['list-panes']

def escape_shell_arg(arg):
    arg = str(arg)
    if re.match(r'^[0-9a-zA-Z,.:_=/-]+$', arg):
        return arg
    else:
        return r"\'".join(f"'{a}'" for a in arg.split("'"))

def escape_shell(lst):
    return ' '.join(escape_shell_arg(arg) for arg in lst)

def make_script(txt, **vars):
    return  ''.join(f"{k}={escape_shell_arg(v)}\n" for k, v in vars.items()) + txt

restore_script = '''\
cd "$pwd"
history -c
history -r "$histf"
echo -ne '\\033c'
echo "=== $name ==="
rm -f "$tempf" "$histf"
unset pwd histf tempf name
_cmd_writehist &> /dev/null
'''

def make_restore(data, sess, w, i, dst, is_new, lst):
    histdat, pwd = data
    tempf_hist = tempfile.NamedTemporaryFile(prefix='restorescn-%s-%d.%d-' % (sess, w, i), suffix='.hist', delete=False)
    tempf_hist.write(histdat)

    tempf = tempfile.NamedTemporaryFile(prefix='restorescn-%s-%d.%d-' % (sess, w, i), suffix='.sh', delete=False)

    tempf.write(make_script(restore_script, pwd=pwd, histf=tempf_hist.name, tempf=tempf.name, name='%s:%d.%d' % (sess, w, i)).encode('utf-8'))
    tempf_hist.close()
    tempf.close()

    cmd = "\n. '%s'\n" % (tempf.name)
    if not is_new:
        cmd = '\x03\x03' + cmd
    if dst is None:
        dst = '%s:%d.%d' % (sess, w, i)

    #cmd = '... %s' % pfx
    if lst is not None:
        lst.append(['send', '-t', dst, cmd])
    return tempf.name

def iterdir(dir, name):
    rxfn = re.compile(r'%s-(\d+)\.(\d+)-hist' % re.escape(name))
    rxfn2 = re.compile(r'%s-(\d+)-hist' % re.escape(name))

    for f in os.listdir(dir):
        m = rxfn.match(f)
        pane = None
        if not m:
            m = rxfn2.match(f)

        if not m:
            continue

        win = int(m.group(1))
        try:
            pane = int(m.group(2))
        except Exception:
            pane = 0

        try:
            with open(join(dir, f), 'rb') as fp:
                histdat = fp.read()
        except Exception:
            continue

        try:
            with open(join(dir, f[:-5] + '-pwd'), 'rb') as fp:
                pwd = fp.readline().decode('utf-8', 'ignore').rstrip('\r\n')
        except Exception:
            continue

        yield win, pane, histdat, pwd

def iterzip(zipf):
    rxfn = re.compile(r'.*?-(\d+)\.(\d+)-hist')
    for f in zipf.namelist():
        m = rxfn.match(f)
        if not m:
            continue
        win = int(m.group(1))
        pane = int(m.group(2))

        try:
            histdat = zipf.read(f)
        except Exception:
            traceback.print_exc()
            continue

        try:
            pwd = zipf.read(f[:-5] + '-pwd').decode('utf-8').rstrip('\r\n')
        except Exception:
            traceback.print_exc()
            continue

        yield win, pane, histdat, pwd


def restore_tmux(args, sess, panes, iter):

    restorewin = {}
    data = {}
    for win, pane, histdat, pwd in iter:
        rpanes = restorewin.get(win)
        if not rpanes:
            rpanes = restorewin[win] = set()
        rpanes.add(pane)
        data[win, pane] = histdat, pwd

    if not restorewin:
        print('Cannot find any save information for %s' % sess)
        return

    exist_windows = set(p.window_index for p in panes)
    new_win = max(set(restorewin) | exist_windows) + 1


    tmux_commands = []
    restoreargs = []

    pane_by_index = dict(((p.window_index, p.line), p) for p in panes)

    if not panes:
        print('Session %s does not exist, creating...' % sess)

        out, code = tmux(args + ['new', '-s', sess, '-d', ';'])
        ok = True
        needfork = False
    else:
        print('Session %s already exists' % sess)
        return

    create_windows = set(restorewin) - exist_windows

    ## first, restore into existing windows
    for w, panes in restorewin.items():
        for i in panes:
            cur_win = pane_by_index.get((w, i))
            if cur_win:
                if cur_win.ok:
                    ## don't send break to pane running this script
                    make_restore(data[w, i], sess, w, i, None, cur_win.is_me, tmux_commands)

    for w, panes in restorewin.items():
        win_id = '%s:%d' % (sess, w)

        if w not in exist_windows:
            fn = make_restore(data[w, 0], sess, w, 0, win_id, True, None)
            tmux_commands.append(['setenv', '-t', sess, 'SCN_RESTORE_SCRIPT', fn])
            tmux_commands.append(['neww', '-k', '-d', '-t', win_id])

        maxw = max(panes)
        for i in range(maxw + 1):
            cur_win = pane_by_index.get((w, i))
            if i not in panes:
                if i > 0:
                    tmux_commands.append(['splitw', '-h', '-t', win_id])
                continue

            if cur_win:
                continue

            if i != 0:
                dst = '%s:%d' % (sess, new_win)
                fn = make_restore(data[w, i], sess, w, i, dst, True, None)
                tmux_commands.append(['setenv', '-t', sess, 'SCN_RESTORE_SCRIPT', fn])
                tmux_commands.append(['neww', '-k', '-d', '-t', dst])

            if i > 0:
                tmux_commands.append(['joinp', '-d', '-h', '-s', dst, '-t', win_id, ';'])

        tmux_commands.append(['setenv', '-t', sess, '-u', 'SCN_RESTORE_SCRIPT', ';'])

    new_wins = []
    if tmux_commands:
        for arglst in tmux_commands:
            out, code = tmux(args + arglst)

    return needfork

def read_session_file(fn, look=None):
    r = ([] if look is None else None)
    sid = None
    with open(fn, 'r') as f:
        for lin in f:
            lst = lin.strip().split(' ')
            if len(lst) < 2:
                if len(lst) == 1:
                    sid = lst[0]
                continue
            name = lst[0]
            if look is not None:
                if name == look:
                    return sid, lst[1:]
            else:
                r.append((name, lst[1:]))
    return sid, r


rxpane = re.compile(r'(\d+)\.(\d+)=(\d+)')
def do_save_session(dir, sessiondir, instancedir, name, dest, ifmtime):
    try:
        sf = join(sessiondir, '%s.session' % name)
        sid, pane_list = read_session_file(sf, name)
        if instancedir is None:
            instancedir = join(dir, 'tmux-%s' % sid)
        if ifmtime:
            for f in os.listdir(instancedir):
                if getmtime(join(instancedir, f)) >= ifmtime:
                    break
            else:
                return
    except IOError:
        print('session not found', file=sys.stderr)
        return


    panes = []
    for l in pane_list:
        m = rxpane.match(l)
        if m:
            panes.append(tuple(int(v) for v in m.groups()))
    if not panes:
        print('no panes!???')
        return

    if dest is None:
        dest = join(dir, '%s.zip' % name)

    zipf = zipfile.ZipFile(dest, 'w', zipfile.ZIP_DEFLATED)
    print('Saving session %s %r' % (name, sorted(set(wid for wid, pn, pid in panes))))
    for wid, pn, pid in panes:
        try:
            zipf.write(join(instancedir, '%d-pwd' % pid), '%s-%d.%d-pwd' % (name, wid, pn))
        except FileNotFoundError:
            pass
        except Exception:
            traceback.print_exc()

        try:
            zipf.write(join(instancedir, '%d-hist' % pid), '%s-%d.%d-hist' % (name, wid, pn))
        except FileNotFoundError:
            pass
        except Exception:
            traceback.print_exc()
    zipf.close()


def save_session(dir, name=None, dest=None, src=None, ifmtime=None):
    if name is None:
        if dest is not None:
            print('cannot use all with --zip', file=sys.stderr)
            return

    if src is not None:
        instancedir = sessiondir = src
    else:
        sessiondir = dir
        instancedir = None

    if name is None:
        lst = os.listdir(sessiondir)
        for fn in lst:
            if fn.endswith('.session'):
                name = fn[:-8]
                fn = join(dir, fn)
                zipf = join(dir, '%s.zip' % name)
                do_save_session(dir, sessiondir, instancedir, name, zipf, (getmtime(zipf) if exists(zipf) else None))
        return

    do_save_session(dir, sessiondir, instancedir, name, dest, None)

def start_log_session(tmux_sock, debug):
    notify_pipe = None
    wait_pipe, notify_pipe = os.pipe()

    cpid = os.fork()
    if cpid != 0:
        # parent process - wait for log-session to fully start up
        os.close(notify_pipe)
        while True:
            try:
                r, w, e = select.select((wait_pipe,), (), (), None)
                if wait_pipe in r:
                    break
            except EnvironmentError as e:
                if e.errno not in RETRY_ERRNO:
                    raise

        return

    os.environ.pop('TMUX', None)
    os.environ.pop('TMUX_INSTANCE', None)

    # child process - run log-session
    os.close(wait_pipe)

    if os.fork() != 0: os._exit(0)
    os.setsid()

    nullf = os.open('/dev/null', os.O_RDWR)
    if debug:
        logf = os.open('/tmp/tmux-log-session.log', os.O_WRONLY|os.O_CREAT|os.O_APPEND)
    else:
        logf = nullf

    os.dup2(nullf, 0)
    os.dup2(logf, 1)
    os.dup2(logf, 2)
    os.close(nullf)
    if debug:
        os.close(logf)

    tc = TmuxControl(tmux_sock, SAVEDIR, debug, notify_pipe)
    try:
        tc.read_command_output()
    except KeyboardInterrupt:
        tc.command('kill-session -t _control', lambda lines: None)
        tc.read_command_output()



def main():
    global separate, tmux_sock
    args = sys.argv[1:]
    if not exists(SAVEDIR):
        os.makedirs(SAVEDIR)

    separate = exists(join(SAVEDIR, 'separate-sessions'))

    options = ArgumentParser()
    options.add_argument('session_args', nargs='*')
    options.add_argument('-s', '--sessionpath', help='path to session')
    options.add_argument('-z', '--zip', help='zip to save or restore session')
    options.add_argument('-H', '--host', help='')
    options.add_argument('-n', '--nodetach', action='store_true', help='launch or relaunch session logger')
    options.add_argument('--remote', help='inner command')
    options.add_argument('-2', '--256color', action='store_true', help='force 256-color mode')
    options.add_argument('--log-session', action='store_true', help='launch or relaunch session logger')
    options.add_argument('--debug', action='store_true', help='write session logger debug output to /tmp/tmux-log-session.log')
    args = options.parse_args()

    save = None
    sock = None
    sess = None
    ls = False
    detach = True
    for a in args.session_args:
        if a in ('s', 'r'):
            save = a
        elif a == 'n':
            args.nodetach = True
        elif a == 'ls':
            ls = True
        elif a.startswith('/'):
            sock = a[1:]
        elif a.startswith(':'):
            sess = a[1:]
        else:
            sess = a

    if separate:
        if sock is None:
            sock = sess
    else:
        if sess is None and sock is not None:
            sess = sock

    preargs = []

    tmux_sock_name = basename(os.environ.get('TMUX', '').split(',')[0]) or None

    if sock is None:
        sock = tmux_sock_name or 'default'

    tmp = os.getenv('TMUX_TMPDIR') or os.getenv('TMPDIR') or '/tmp'
    sock_dir = join(tmp, 'tmux-%d' % (os.geteuid()))
    if not exists(sock_dir):
        os.mkdir(sock_dir, mode=0o700)
    tmux_sock = join(sock_dir, sock)

    if args.log_session:
        start_log_session(tmux_sock, args.debug)
        return

    if args.remote:
        attach_args = ['-2', 'attach']
        if not args.nodetach:
            attach_args.append('-d')
        attach_args.append('-t')
        attach_args.append(args.remote)
        out, rcode = tmux(attach_args, capture=False, host=args.host)
        if rcode != 0:
            rcode = tmux(['-2', 'new', '-s', args.remote], capture=False, host=args.host)
        tmux(['detach'])
        return

    if args.host:
        if save:
            print(f'Cannot save or restore on remote')

        csock = get_ssh_sock(args.host)
        # Check if there is a master running on the given
        p = runproc(['ssh', '-S', csock, '-O', 'check', ''], capture=True)
        if p.returncode != 0:
            p = runproc(['ssh', '-M', '-o', 'ControlPersist=yes', '-o', f'ControlPath={csock}', '-n', '-f', '-T', '-N', args.host], capture=False)
            if p.returncode != 0:
                print(f'Could not connect master to {args.host}')
                return

    sessions = ListSessions.run(preargs, host=args.host)
    sess_by_name = dict((s.session_name, s) for s in sessions)

    ## Linux VT is the only terminal I can find that *doesn't* support 256 colors
    if not os.environ.get('TERM', '').startswith('linux'):
        preargs.append('-2')

    if save:
        panes = Pane.run(preargs, ['-a'])
        existing_session = bool(panes)

        if not sess:
            mypane = os.getenv('TMUX_PANE')
            if not mypane or tmux_sock_name != sock:
                print('not in tmux and none specified')
                return

            mysess = [p.session_name for p in panes if p.pane_id == mypane]
            if len(mysess) > 1:
                print('pane is in multiple sessions (%s)' % ', '.join(mysess))
                return

            if not mysess:
                print('pane could not be found')
                return

            sess = mysess[0]
        panes = [p for p in panes if p.session_name == sess]

        if save == 'r':
            if not '_control' in sess_by_name:
                start_log_session(tmux_sock, args.debug)

            defaultzip = join(SAVEDIR, '%s.zip' % sess)
            zip = args.zip
            if zip is None and exists(defaultzip):
                zip = defaultzip

            if zip is not None:
                itr = iterzip(zipfile.ZipFile(zip, 'r'))
            else:
                itr = iterdir(SAVEDIR, sess)
            restore_tmux(preargs, sess, panes, itr)
            return
        else:
            if not os.path.isdir(SAVEDIR):
                os.makedirs(SAVEDIR)
            if sess == 'all':
                sess = None
            return save_session(SAVEDIR, sess, args.zip, args.sessionpath)

    if ls or (sess is None):
        for s in sessions:
            if s.session_name == '_control':
                continue
            print('%-10s: %2d win (created %s) %s' % \
                (s.session_name, s.session_windows, s.session_created_string,
                 ' attached' if s.session_attached else ''))
        return

    if args.host:
        sessname = '_' + os.urandom(8).hex()
        remote_args = list(preargs)
        remote_args.extend(['new-session', '-P', '-d',  '-s', sessname, '--', __file__, '--remote', sess, '-H', args.host])
        if args.nodetach:
            remote_args.append('--nodetach')

        #print(' '.join(remote_args))
        tmux(remote_args)
        tmux([
            'set-option', '-t', sessname, 'status', 'off', ';',
            'set-option', '-t', sessname, f'set-titles-string', f"[RMT {args.host}] #T", ';',
            'set-option', '-t', sessname, 'prefix', 'C-q',
        ], capture=False)

        # just needs to be present
        sess_by_name[sessname] = True
        args.nodetach=True
        sess = sessname

    if sock == tmux_sock_name:
        del os.environ['TMUX']

        if sess in sess_by_name:
            if not args.nodetach:
                tmux(preargs + ['detach-client', '-s', sess])
        else:
            tmux(preargs + ['new-session', '-d', '-s', sess])
        os.execv(TMUX, [TMUX, '-S', tmux_sock] + preargs + ['switch-client', '-t', sess])
    else:
        if not '_control' in sess_by_name:
            start_log_session(tmux_sock, args.debug)

        if sess in sess_by_name:
            preargs.append('attach')
            if not args.nodetach:
                preargs.append('-d')
            os.execvp(TMUX, [TMUX, '-S', tmux_sock] + preargs + ['-t', sess])
        else:
            os.execvp(TMUX, [TMUX, '-S', tmux_sock] + preargs + ['new', '-s', sess])

main()
