"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math

def square_root(a):
    try:
        if a < 0:
            raise ValueError("Cannot get root of a negative number")

        return math.sqrt(a)

    except ValueError as e:
        print(e)

def hypotenuse(a,b):

    return math.hypot(a,b)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by 0")

    return b / a

def logarithm(a, b):
    if a <= 1:
        raise ValueError("Base cannot be <= 1")

    if b <= 0:
        raise ValueError("Argument cannot be <= 0")

    return math.log(b, a)  # log base a of b

def exponent(a, b):
    return math.pow(a, b)

