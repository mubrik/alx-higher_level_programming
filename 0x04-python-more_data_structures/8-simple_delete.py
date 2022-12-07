#!/usr/bin/python3


def simple_delete(a_dictionary: dict, key=""):
    """ delete a key in dictionary, what a weird func """
    if not a_dictionary:
        return a_dictionary
    if key in a_dictionary.keys():
        del a_dictionary[key]
    return a_dictionary
