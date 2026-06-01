import pytest
from working import convert

def test_convert():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00", "expected 09:00 to 17:00"
    assert convert("12:00 PM to 12:00 AM") == "12:00 to 00:00", "expected 12:00 to 00:00"
    assert convert("1:30 PM to 2:45 PM") == "13:30 to 14:45", "expected 13:30 to 14:45"
    assert convert("11:59 PM to 12:01 AM") == "23:59 to 00:01", "expected 23:59 to 00:01"
    with pytest.raises(ValueError):
        convert("9:00 to 5:00")
    with pytest.raises(ValueError):
        convert("9:00 AM to 5:00")
    with pytest.raises(ValueError):
        convert("9:00 to 5:00 PM")
def test_no_minutes():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00", "expected 09:00 to 17:00"
    assert convert("12 PM to 12 AM") == "12:00 to 00:00", "expected 12:00 to 00:00"
    assert convert("1 PM to 2 PM") == "13:00 to 14:00", "expected 13:00 to 14:00"
    assert convert("11 PM to 12 AM") == "23:00 to 00:00", "expected 23:00 to 00:00"

def test_invalid_format():
    with pytest.raises(ValueError):
        convert("9:00 to 5:00")
    with pytest.raises(ValueError):
        convert("9:00 AM to 5:00")
    with pytest.raises(ValueError):
        convert("9:00 to 5:00 PM")