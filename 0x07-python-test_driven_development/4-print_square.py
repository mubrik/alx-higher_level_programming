#!/usr/bin/python3
""" This is print_square module

The module supplies one function, print_square().

>>> print_square(1)
#
"""

raiseErr = TypeError("size must be an integer")


def print_square(size):
    """ Write a function that prints a square with the character #.
    >>> print_square(1)
    #
    """
    if not isinstance(size, int):
        raise raiseErr
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        return
    else:
        for i in range(size):
            print("#" * size)
