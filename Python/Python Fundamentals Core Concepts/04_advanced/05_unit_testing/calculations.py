# calculations.py
def add(a, b):  # type:ignore
    return a + b  # type:ignore


def subtract(a, b):  # type:ignore
    return a - b  # type:ignore


def multiply(a, b):  # type:ignore
    return a * b  # type:ignore


def divide(a, b):  # type:ignore
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b  # type:ignore