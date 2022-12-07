#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary: dict | None):
    """ print a sorted dictionary """
    if not a_dictionary:
        return 0
    for key in sorted(a_dictionary.keys()):
        print(f"{key}: {str(a_dictionary[key])}")
