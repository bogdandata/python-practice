import pytest
from numb3rs import validate

def test_validate():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True
    assert validate("256.1.1.1") == False
    assert validate("1.256.1.1") == False
    assert validate("1.1.256.1") == False
    assert validate("1.1.1.256") == False
    assert validate("1.1.1") == False
    assert validate("1.1.1.1.1") == False
    assert validate("abc.def.ghi.jkl") == False
    assert validate("123.456.78.90") == False