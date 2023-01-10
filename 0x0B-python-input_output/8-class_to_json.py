#!/usr/bin/python3
""" Working with Files and JSON """


def class_to_json(obj):
    """ class to serializable struct """
    return vars(obj)
