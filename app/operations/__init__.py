# app/operations.py

from typing import Union 

Number = Union[int, float]

def add(a: Number, b: Number) -> Number:
    result = a + b
    return result

def subtract(a: Number, b: Number) -> Number:
    result = a - b
    return result

def multiply(a: Number, b: Number) -> Number:
    result = a * b
    return result

def divide(a: Number, b: Number) -> float:
    if b == 0:
        # Raise a ValueError with a descriptive message
        raise ValueError("Cannot divide by zero!")
    result = a / b
    return result
