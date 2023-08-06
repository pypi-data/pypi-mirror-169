import pytest
from inline_files import InlineFiles, InvalidFormatError

ilf = InlineFiles()

def test_inline_file():
    assert ilf.get_file("ID1") == "Hello World!\n"
    
def test_inline_file_list():
    assert eval(ilf.get_file("ID2")) == [1,2,3,4]

def test_empty_inline_file():
    assert ilf.get_file("ID3") == ""

def test_non_existant_inline_file():
    assert ilf.get_file("ID4") == None

def test_valid_file():
    ilf = InlineFiles(file="test/valid.py")
    assert ilf.get_file("ID1") == "This should work!\n"

def test_invalid_file():
    try:
        InlineFiles(file="test/dummy.py")
        assert False
    except InvalidFormatError:
        assert True

r"""ILF
__ID1__
Hello World!
__ID2__
[1,2,3,4]
__ID3__
"""