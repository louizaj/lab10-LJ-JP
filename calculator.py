#https://github.com/louizaj/lab10-LJ-JP.git
#Partner 1: Louiza Joya
#Partner 2: Joseph Patriarca

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

import math

# First example
def add(a, b):
    return a + b

def sub(a, b):
    return a - b
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

def logarithm(a, b):
    if a <= 1:
        raise ValueError("Base cannot be <= 1")

    if b <= 0:
        raise ValueError("Argument cannot be <= 0")

    return math.log(b, a)  # log base a of b

def exponent(a, b):
    return math.pow(a, b)

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a

def log(a, b):
    if b <= 0:
        raise ValueError("Cannot perform logarithm on negative numbers")
    if a < 1:
        raise ValueError("Logarithm is not defined for base of 1 or less")
    return math.log(b, a)

def exp(a, b):
    return a ** b