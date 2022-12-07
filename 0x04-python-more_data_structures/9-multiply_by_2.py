#!/usr/bin/python3


def multiply_by_2(a_dictionary: dict):
    """ multiply all values by 2 and return new dict """
    if not a_dictionary:
        return a_dictionary
    return dict(zip(a_dictionary.keys(),
                    [x * 2 for x in a_dictionary.values()]))
