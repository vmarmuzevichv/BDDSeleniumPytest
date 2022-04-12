import pytest
import sys
const = 9/5

def cent(cent=0):
    fah = (cent * const) + 32
    return fah



@pytest.mark.skip(reason="huinya kakaya to")
def test01():
    assert  type(const) == float

def test02():
    assert  cent() == 32

def test03():
    assert  cent(38) == 100.4