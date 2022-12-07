#!/usr/bin/python3


def update_dictionary(a_dictionary, key, value):
    """ update a dictionary, what a weird func """
    if not a_dictionary:
        return a_dictionary
    if key:
        a_dictionary[key] = value
    return a_dictionary
