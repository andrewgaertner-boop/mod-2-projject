import pytest

from calculator import (
    Addition,
    Subtraction,
    Multiplication,
    Division,
    CalculationFactory,
    show_help,
    show_history
)


# -------------------------
# Basic Calculation Tests
# -------------------------

def test_add():
    calculation = Addition(10, 5)
    assert calculation.execute() == 15


def test_subtract():
    calculation = Subtraction(10, 5)
    assert calculation.execute() == 5


def test_multiply():
    calculation = Multiplication(10, 5)
    assert calculation.execute() == 50


def test_divide():
    calculation = Division(10, 5)
    assert calculation.execute() == 2


def test_divide_by_zero():
    calculation = Division(10, 0)

    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculation.execute()


# -------------------------
# CalculationFactory Tests
# -------------------------

def test_factory_addition():
    calculation = CalculationFactory.create("+", 10, 5)

    assert isinstance(calculation, Addition)
    assert calculation.execute() == 15


def test_factory_subtraction():
    calculation = CalculationFactory.create("-", 10, 5)

    assert isinstance(calculation, Subtraction)
    assert calculation.execute() == 5


def test_factory_multiplication():
    calculation = CalculationFactory.create("*", 10, 5)

    assert isinstance(calculation, Multiplication)
    assert calculation.execute() == 50


def test_factory_division():
    calculation = CalculationFactory.create("/", 10, 5)

    assert isinstance(calculation, Division)
    assert calculation.execute() == 2


def test_factory_invalid_operator():
    with pytest.raises(ValueError, match="Invalid operation"):
        CalculationFactory.create("%", 10, 5)


# -------------------------
# Help Command Test
# -------------------------

def test_help(capsys):
    show_help()

    captured = capsys.readouterr()

    assert "help" in captured.out
    assert "history" in captured.out
    assert "exit" in captured.out


# -------------------------
# History Test
# -------------------------

def test_empty_history(capsys):
    show_history([])

    captured = capsys.readouterr()

    assert "No calculations yet." in captured.out