from __future__ import print_function
from os.path import exists
import os
import os.path
import pdb


_unset = object()


def get_curindex(self):
    if 'curindex' in self.__dict__:
        self._curindex = self.__dict__.pop('curindex')
        # the property didn't exist before
        launch(self)
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
        launch(self)


def patch():
    pdb.Pdb.curindex = property(get_curindex, set_curindex)
    pdb.Pdb._original_preloop = pdb.Pdb.preloop
    pdb.Pdb._original_precmd = pdb.Pdb.precmd
    pdb.Pdb.preloop = preloop
    pdb.Pdb.precmd = precmd


def launch(self):
    try:
        (frame, lineno) = self.stack[self.curindex]
    except IndexError:
        return
    filename = self.canonic(frame.f_code.co_filename)
    if exists(filename):
        command = 'subl -b "%s:%d"' % (filename, lineno)
        os.system(command)


def preloop(self):
    launch(self)
    return self._original_preloop()


def precmd(self, line):
    launch(self)
    return self._original_precmd(line)
