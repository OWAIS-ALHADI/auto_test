import pytest
from calcul import add, subtract, multiply

def test_add():
    assert add(3, 4) == 7
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(10, 4) == 6
    assert subtract(0, 5) == -5

def test_multiply():
    assert multiply(3, 5) == 15
    assert multiply(-1, 8) == -8
