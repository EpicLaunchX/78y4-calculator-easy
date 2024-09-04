# domain/models.py
from dataclasses import dataclass


@dataclass
class Operand:
    first_operand: int
    second_operand: int
