# tests/test_models.py
import pytest

# imports must be sorted correctly
from src.pytemplate.domain.models import Operand


# initial values
def test_operand_assignment():
    # initialization requires two values
    operand = Operand(42, 15)
    assert operand.first_operand == 42
    assert operand.second_operand == 15


# class fields will hold numeric values
def test_operand_reassignment():
    operand = Operand(42, 15)
    # reassignment
    operand.first_operand = 5
    assert operand.first_operand == 5
    assert operand.second_operand == 15


# class fields will ERROR if assigned non-numeric values
def test_operand_assignment_non_int():
    operand = Operand(42, 15)
    with pytest.raises(TypeError):
        operand.first_operand = "not an integer"
        operand.second_operand = "also not an integer"
