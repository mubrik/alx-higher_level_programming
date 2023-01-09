#!/usr/bin/python3
""" This is lookup module

The module supplies one function, lookup().
A function that returns the list of available attributes and methods of an obj

>>> lookup(obj)
[...]
"""


def lookup(obj):
    """  returns the list of available attributes and methods of an object
    >>> lookup()
    [...]
    """
    return dir(obj)
