#!/usr/bin/python3


def best_score(a_dictionary: dict):
    """ Write a function that returns a key with the biggest integer value. """
    if not a_dictionary:
        return None
    return sorted(a_dictionary.items(), key=lambda x: x[1], reverse=True)[0][0]
