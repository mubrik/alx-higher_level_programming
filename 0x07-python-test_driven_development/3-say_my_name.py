#!/usr/bin/python3
""" This is say_my_name module

The module supplies one function, say_my_name().

>>> say_my_name("Mr", "Mubrik")
My name is Mr Mubrik
"""


def say_my_name(first_name, last_name=""):
    """ Write a function that prints My name is <first name> <last name>
    >>> say_my_name("Mr")
    My name is Mr
    >>> say_my_name("Mr", "Mubrik")
    My name is Mr Mubrik
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
