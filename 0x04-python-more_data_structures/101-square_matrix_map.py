#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda el: map(lambda x: x**2, el), matrix))
