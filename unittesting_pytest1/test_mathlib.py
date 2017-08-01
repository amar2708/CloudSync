import mathlib


def test_add():
    total = mathlib.add(10, 20)
    assert total == 30


def test_multiply():
    result = mathlib.multiply(10, 10)
    assert result == 100
