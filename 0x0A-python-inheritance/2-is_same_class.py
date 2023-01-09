#!/usr/bin/python3
""" This is is_same_class module

The module supplies one class, is_same_class().
A function that returns True if the obj is exactly an instance of the class

>>> is_same_class(obj, a_class)
True
"""


def is_same_class(obj, a_class):
    """ fucntion check if obj is exactly of class """
    return type(obj) == a_class
