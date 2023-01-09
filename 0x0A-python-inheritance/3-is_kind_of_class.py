#!/usr/bin/python3
""" This is is_kind_of_class module

The module supplies one class, is_kind_of_class().
A function that returns True if the obj is an instance of the class

>>> is_kind_of_class(obj, a_class)
True
"""


def is_kind_of_class(obj, a_class):
    """ fucntion check if obj is instance of class """
    return isinstance(obj, a_class)
