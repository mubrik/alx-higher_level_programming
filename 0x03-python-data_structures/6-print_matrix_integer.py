#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for j, col in enumerate(row):
            print("{}{:d}".format(" " if j != 0 else "", col), end="")
        print()  # new line
