#!/usr/bin/python3


def complex_delete(a_dictionary: dict, value):
    if not a_dictionary:
        return None
    for key in [key for key, val in a_dictionary.items() if val == value]:
        del a_dictionary[key]
    return a_dictionary
