#!/usr/bin/python3
from sys import stderr


def safe_print_integer_err(value):
    """Write a function that prints an integer safely."""
    try:
        print("{:d}".format(value))
        return True
    except Exception as ex:
        err = f"Exception: {ex.__str__()}\n"
        stderr.write(err)
        return False
