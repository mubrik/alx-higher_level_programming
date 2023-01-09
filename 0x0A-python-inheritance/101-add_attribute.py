#!/usr/bin/python3
""" Write a function that adds a new attribute to an object if possible: """


def add_attribute(obj, name, value):
    """ try set """
    if "__dict__" not in dir(obj):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
