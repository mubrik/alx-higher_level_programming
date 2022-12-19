#!/usr/bin/python3


def safe_print_integer(value):
    """Write a function that prints an integer with "{:d}".format()"""
    if not isinstance(value, int):
        return False
    try:
        print("{:d}".format(value))
    except Exception:
        return False
    return True
