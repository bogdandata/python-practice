import pytest
from fuel import convert, gauge

def test_convert():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
    assert convert("1/4") == 25, "expected 25"
    assert convert("3/4") == 75, "expected 75"
    assert convert("0/1") == 0, "expected 0"
    assert convert("1/1") == 100, "expected 100"
    with pytest.raises(ValueError):
        convert("2/1")

def test_gauge():
    assert gauge(0) == "E", "expected E"
    assert gauge(1) == "E", "expected E"
    assert gauge(2) == "2%", "expected 2%"
    assert gauge(50) == "50%", "expected 50%"
    assert gauge(98) == "98%", "expected 98%"
    assert gauge(99) == "F", "expected F"
    assert gauge(100) == "F", "expected F"
