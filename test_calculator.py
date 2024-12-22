import pytest
from calculator import multiply, divide

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 5) == -5
    assert multiply(0, 10) == 0

def test_divide():
    assert divide(6, 3) == 2
    assert divide(10, -2) == -5
    with pytest.raises(ValueError):
        divide(5, 0)

