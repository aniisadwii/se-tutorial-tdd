def add(a, b): 
    c = a + b;
    return c


def subtract(a, b):
    c = a - b;
    return c


def multiply(a, b):
    c = a * b;
    return c


def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    c = a / b;
    return c
