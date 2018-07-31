from PdbEditorSupport import patch
import pytest


@pytest.fixture
def MyPdb():
    import pdb

    class MyPdb(pdb.Pdb):
        pass

    return MyPdb


def get_stack():
    import sys
    stack = []
    frame = sys._getframe()
    while frame:
        stack.insert(0, (frame, frame.f_lineno))
        frame = frame.f_back
    return stack


def test_double_patch(MyPdb):
    orig_preloop = MyPdb.preloop
    orig_precmd = MyPdb.precmd
    patch(editor='sublime', _class=MyPdb)
    assert MyPdb._original_preloop == orig_preloop
    assert MyPdb._original_precmd == orig_precmd
    patch(editor='sublime', _class=MyPdb)
    assert MyPdb._original_preloop == orig_preloop
    assert MyPdb._original_precmd == orig_precmd


def test_property(MyPdb):
    instance = MyPdb()
    instance.reset()
    assert instance.curindex == 0
    instance.stack[:] = get_stack()
    calls = []
    patch(func=lambda *a, **k: calls.append((a, k)), _class=MyPdb)
    instance.curindex = 1
    instance.curindex = 2
    assert instance.curindex == 2
    assert len(calls) == 2
