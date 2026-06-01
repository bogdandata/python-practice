import pytest
from seasons import main, minutes

def test_main(monkeypatch, capsys):
    inputs = ["2000-01-01", "1990-05-15", "1985-10-30", "1975-12-25", "1960-07-04"]
    expected_outputs = [
        "You have lived for one million fifty-one thousand eight hundred and ninety-six minutes.",
        "You have lived for one million six hundred ninety-three thousand four hundred minutes.",
        "You have lived for one million nine hundred thirty-five thousand three hundred and sixty minutes.",
        "You have lived for two million five hundred twenty-two thousand eight hundred minutes.",
        "You have lived for three million one hundred fifty-three thousand six hundred minutes."
    ]
    

def test_minutes():
    from datetime import date
    today = date.today()
    birth = date(2000, 1, 1)
    expected = (today - birth).days * 24 * 60
    assert minutes("2000-01-01") == expected

def test_invalid_date():
    with pytest.raises(ValueError):
        minutes("2000-13-01")
    with pytest.raises(ValueError):
        minutes("1990-00-15")
    with pytest.raises(ValueError):
        minutes("1985-10-32")
    with pytest.raises(ValueError):
        minutes("1975-12-00")
    with pytest.raises(ValueError):
        minutes("1960-07-40")