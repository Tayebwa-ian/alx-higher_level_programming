#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    mat = [[j[i]**2 for i in range(len(j))] for j in matrix]
    return mat
