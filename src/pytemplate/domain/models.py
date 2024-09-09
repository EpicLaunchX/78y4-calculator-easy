# domain/models.py
from dataclasses import dataclass


@dataclass
class Operand():
    # Init function just assigns value
    def __init__(self, first_operand: int, second_operand: int):
        self.first_operand = first_operand
        self.second_operand = second_operand
        
    # SetAttr function performs type validation
    def __setattr__(self, attr, value):
        if not isinstance(value, int):
            raise TypeError(f'{attr} must be type int')
        super().__setattr__(attr, value)
