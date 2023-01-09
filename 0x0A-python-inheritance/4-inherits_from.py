#!/usr/bin/python3
""" This is inherits_from module

The module supplies one class, inherits_from().
A function that returns True if the object is an instance
of a class that inherited (directly or indirectly) from the specified class

>>> inherits_from(obj, a_class)
True
"""


def inherits_from(obj, a_class):
    """ fucntion check if obj is instance of class """
    return isinstance(obj, tuple(a_class.__subclasses__()))
