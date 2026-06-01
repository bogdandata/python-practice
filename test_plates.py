from plates import is_valid

def test_too_short():
    assert not is_valid("A")

def test_valid():
    assert is_valid("AA") == True

def test_too_long():
    assert not is_valid("AAAAAAA")

def test_first_two_letters():
    assert not is_valid("1A") 
    assert not is_valid("A1")

def test_non_zero_digit():
    assert not is_valid("0000") 
    assert is_valid("AAA1")