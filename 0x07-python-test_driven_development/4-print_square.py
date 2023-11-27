#!/usr/bin/python3
"""Print square module"""


def print_square(size):
    """prints a square with the character #
    Args:
      size: size of the square side
    Raises:
      TypeError: if size is not an in
    Returns: None
    """
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
