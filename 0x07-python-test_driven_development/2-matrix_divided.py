#!/usr/bin/python3
"""Divide a matrix Module"""


def matrix_divided(matrix, div):
    """ divides matrix elements y the given integer div
    Args:
      -matrix: the matrix
      -div: the given integer to use
    Raises:
      -TypeError: -if matrix is not a list of lists
                   with integer or float elements
                  -raises same error if elements of the outer matrix
                   differ in size
                  -raises same error if div is not int or float
      -ZeroDivisionError: if div is zero
    Return:
      -new matrix
    """
    lst = [int, float]
    if type(div) not in lst:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) is not list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if len(matrix) < 2:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    size = len(matrix[0])
    for el in matrix:
        if type(el) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        if len(el) != size:
            raise TypeError(
                "Each row of the matrix must have the same size")
        for i in el:
            if type(i) not in lst:
                raise TypeError("matrix must be a matrix "+
                                "(list of lists) of integers/floats")
    new_matrix = [list(map(lambda x: round(x/div, 2), el)) for el in matrix]
    return new_matrix
