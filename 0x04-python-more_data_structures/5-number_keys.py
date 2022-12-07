#!/usr/bin/python3


def number_keys(a_dictionary):
    """ get number of keys in a dict """
    if not a_dictionary:
        return 0
    return len(a_dictionary.keys())
