# domain/models.py
from dataclasses import dataclass


@dataclass
class Operand:
    # Proper init function to validate input
    def __init__(self, first_operand: int, second_operand: int):
        # Raises error if value is not an integer
        if not isinstance(first_operand, int):
            raise TypeError("first_operand must be an integer")
        if not isinstance(second_operand, int):
            raise TypeError("second_operand must be an integer")
        # Assigns values to class object
        self.first_operand = first_operand
        self.second_operand = second_operand
