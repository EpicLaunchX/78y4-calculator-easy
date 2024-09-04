# tests/test_models.py
import pytest
from src.pytemplate.domain.models import Operand


# initialization should always set class fields to 0
def test_operand_initialization():
    operand = Operand()
    assert operand.first_operand == 0
    assert operand.second_operand == 0


# class fields will hold numeric values
def test_operand_assignment():
    operand = Operand()
    operand.first_operand = 42
    operand.second_operand = 15
    assert operand.first_operand == 42
    assert operand.second_operand == 15


# class fields will ERROR if assigned non-numeric values
def test_operand_assignment_non_int():
    with pytest.raises(TypeError):
        operand.first_operand = "not an integer"
        operand.second_operand = "also not an integer"
