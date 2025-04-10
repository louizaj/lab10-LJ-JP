#https://github.com/louizaj/lab10-LJ-JP.git
#Partner 1: Louiza Joya
#Partner 2: Joseph Patriarca

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

import math

def add(a, b):
    return a + b

def square_root(a):
    # try:
    if a < 0:
        raise ValueError

    return math.sqrt(a)

    # except ValueError as e:
    #     print(e)

def hypotenuse(a,b):
    return math.hypot(a,b)

def subtract(a, b):
    return a - b

def logarithm(a, b):
    if a <= 1:
        raise ValueError

    if b <= 0:
        raise ValueError

    return math.log(b, a)  # log base a of b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a

def exp(a, b):
    return a ** b