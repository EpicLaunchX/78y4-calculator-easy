# domain/models.py
from dataclasses import dataclass


# need a class for this
@dataclass
class Operand:
    first_operand: int
    second_operand: int
