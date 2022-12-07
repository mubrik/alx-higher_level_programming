#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    if not matrix:
        return matrix
    new_matrix = []
    for row in matrix:
        new_matrix.append(list(map(lambda x: pow(x, 2), row)))
    return new_matrix
