#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    """Write a function that executes a function safely."""
    result = None
    if not fct:
        return result
    # execute
    try:
        result = fct(*args)
    except Exception as ex:
        err = f"Exception: {ex.__str__()}\n"
        stderr.write(err)
        result = None
    finally:
        return result
