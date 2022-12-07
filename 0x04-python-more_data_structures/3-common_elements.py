#!/usr/bin/python3


def common_elements(set_1, set_2):
    """ get common elem in a set """
    if set_1 is None and set_2 is None:
        return "Stop trolling Alx"
    return set.intersection(set_1, set_2)
