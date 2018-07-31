from PdbEditorSupport import patch
import pytest


@pytest.fixture
def MyPdb():
    import pdb

    class MyPdb(pdb.Pdb):
        pass

    return MyPdb


def test_double_patch(MyPdb):
    orig_preloop = MyPdb.preloop
    orig_precmd = MyPdb.precmd
    patch(editor='sublime', _class=MyPdb)
    assert MyPdb._original_preloop == orig_preloop
    assert MyPdb._original_precmd == orig_precmd
    patch(editor='sublime', _class=MyPdb)
    assert MyPdb._original_preloop == orig_preloop
    assert MyPdb._original_precmd == orig_precmd
