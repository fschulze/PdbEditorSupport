from __future__ import print_function
from functools import partial
import os.path
import subprocess


_unset = object()


def get_curindex(self):
    if 'curindex' in self.__dict__:
        self._curindex = self.__dict__.pop('curindex')
        # the property didn't exist before
        _launch_editor(self)
    return self._curindex


def set_curindex(self, index):
    if 'curindex' in self.__dict__:
        self.__dict__.pop('curindex')
        # the property didn't exist before
        _curindex = _unset
    elif hasattr(self, '_curindex'):
        _curindex = self._curindex
    else:
        _curindex = _unset
    self._curindex = index
    if (_curindex != index):
        _launch_editor(self)


def patch(**kw):
    _class = kw.pop('_class', None)
    if _class is None:
        import pdb
        _class = pdb.Pdb
    if hasattr(_class, '_pdbeditorsupport'):
        return
    if 'func' in kw and 'editor' in kw:
        print("Both 'func' and 'editor' set for PdbEditorSupport, using 'func'.")
    editor = kw.pop('editor', None)
    if editor == 'sublime':
        func = 'shell'
        kw.setdefault('command', 'subl')
        kw.setdefault('command_args', ['-b', '{filename}:{lineno}'])
    elif editor == 'textmate':
        func = 'shell'
        kw.setdefault('application', 'TextMate')
        kw.setdefault(
            'url',
            'txmt://open?url=file://{filename}&line={lineno}&column=2')
        kw.setdefault(
            'apple_scriptcommand',
            'tell application "{application}" to get url "{url}"')
        kw.setdefault('command', 'osascript')
        kw.setdefault(
            'command_args',
            ['-e', '{apple_scriptcommand}'])
    else:
        func = None
    func = kw.pop('func', func)
    if func == 'shell':
        func = shell
    if func is None:
        print("No 'func' or 'editor' set for PdbEditorSupport, can't patch.")
        return
    global _launch_editor
    _launch_editor = partial(_launch, func=func, **kw)
    _class.curindex = property(get_curindex, set_curindex)
    _class._original_preloop = _class.preloop
    _class._original_precmd = _class.precmd
    _class.preloop = preloop
    _class.precmd = precmd
    _class._pdbeditorsupport = True


def shell(filename, lineno, command, command_args, **kw):
    args = [command] + list(command_args)
    while 1:
        newargs = list(
            x.format(filename=filename, lineno=lineno, **kw)
            for x in args)
        changed = (newargs != args)
        args = newargs
        if not changed:
            break
    subprocess.call(args)


def _launch(self, func, **kw):
    try:
        (frame, lineno) = self.stack[self.curindex]
    except IndexError:
        return
    filename = self.canonic(frame.f_code.co_filename)
    if os.path.exists(filename):
        func(filename, lineno, **kw)


def preloop(self):
    _launch_editor(self)
    return self._original_preloop()


def precmd(self, line):
    _launch_editor(self)
    return self._original_precmd(line)
