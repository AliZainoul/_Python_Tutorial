# tests/test_calculator.py

import pytest
from src.calculate import Calculator

def test_add():
    calc = Calculator()
    assert calc.add(1, 2) == 3

def test_subtract():
    calc = Calculator()
    assert calc.subtract(5, 2) == 3

def test_multiply():
    calc = Calculator()
    assert calc.multiply(3, 4) == 12

def test_divide():
    calc = Calculator()
    assert calc.divide(10, 2) == 5

def test_divide_by_zero():
    calc = Calculator()
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.divide(10, 0)

def test_perform_operation():
    calc = Calculator()
    assert calc.perform_operation("add", 1, 2) == 3
    assert calc.perform_operation("subtract", 5, 2) == 3
    assert calc.perform_operation("multiply", 3, 4) == 12
    assert calc.perform_operation("divide", 10, 2) == 5
    assert calc.perform_operation("power", 2, 3) == 8

    with pytest.raises(ValueError, match="Operation unknown not supported"):
        calc.perform_operation("unknown", 1, 2)
