#!/usr/bin/python3
""" This is matrix_divided module

The module supplies one function, matrix_divided().

>>> matrix_divided([[10, 10, 20], [10, 10, 20]], 2)
[[5.0, 5.0, 10.0], [5.0, 5.0, 10.0]]
>>> matrix_divided([[2, 2, 20], [2.0, 2.0, 2.0]], 2)
[[5.0, 5.0, 10.0], [5.0, 5.0, 10.0]]
"""

# custom rror to avoid repeat
customErr = TypeError(
    "matrix must be a matrix (list of lists) of integers/floats"
)


def matrix_divided(matrix, div):
    """ Write a function that divides all elements of a matrix.
    >>> matrix_divided([[10, 10, 20], [10, 10, 20]], 2)
    [[5.0, 5.0, 10.0], [5.0, 5.0, 10.0]]
    >>> matrix_divided([[2, 2, 20], [2.0, 2.0, 2.0]], 2)
    [[1.0, 1.0, 10.0], [1.0, 1.0, 1.0]]
    """
    fin_matrix = []
    if not isinstance(div, int):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not matrix or not isinstance(matrix, list)\
            or not isinstance(matrix[0], list):
        raise customErr
    # matrix[0] is sure to be a list here
    first_len = len(matrix[0])
    for row in matrix:
        new_row = [0 for _ in range(first_len)]
        if len(row) != first_len:
            raise TypeError("Each row of the matrix must have the same size")
        try:
            for index, num in enumerate(row):
                if not isinstance(num, (int, float)):
                    raise customErr
                new_row[index] = round(num / div, 2)
            fin_matrix.append(new_row)
        except Exception:
            raise customErr
    return fin_matrix
