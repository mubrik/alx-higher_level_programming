#!/usr/bin/python3


def safe_print_division(a, b):
    """Write a function that divides 2 integers and prints the result.."""
    result = None
    try:
        result = a / b
    except Exception:
        return None
    finally:
        print("Inside result: {}".format(result))
        return result
