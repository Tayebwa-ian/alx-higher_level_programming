#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda el: [x**2 for x in el], matrix))
