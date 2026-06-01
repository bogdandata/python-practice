import pytest
from um import count

def test_um():
    assert count("um") == 1
    assert count("Um") == 1
    assert count("UM") == 1
    assert count("um um") == 2
    assert count("um, um, um!") == 3
    assert count("um?") == 1

def test_no_um():
    assert count("hello world") == 0
    assert count("this is a test") == 0
    assert count("python programming") == 0
    assert count("umumum") == 0

def test_um_in_words():
    assert count("umbrella") == 0
    assert count("aluminum") == 0
    assert count("umami") == 0
    assert count("umlaut") == 0