#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    """ get symettric diference of items in set """
    if set_1 is None and set_2 is None:
        return "Stop trolling Alx"
    return set.symmetric_difference(set_1, set_2)
