#!/usr/bin/python3
"""Add two integres"""


def add_integer(a, b=98):
    """Add two integers
    Args:
      -a: first integer
      -b: second integer
    Raises:
      -TypeError if a or b in neither float or int
    Return: sum of two integers
    """
    lst = [int, float]
    if type(a) not in lst:
        raise TypeError("a must be an integer")
    if type(b) not in lst:
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
