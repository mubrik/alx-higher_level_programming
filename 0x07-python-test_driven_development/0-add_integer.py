#!/usr/bin/python3
""" This is add_integer module

The module supplies one function, add_integer().

>>> add_integer(5, 100)
105
"""


def add_integer(a, b=98):
    """ Write a function that adds 2 integers.
    >>> add_integer(10)
    108
    >>> add_integer(10, 200)
    210
    >>> add_integer(None)
    Traceback (most recent call last):
    ...
    TypeError:
    """
    # initail check
    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, int):
        raise TypeError("b must be an integer")
    # cast both
    a, b = int(a), int(b)
    return a + b
