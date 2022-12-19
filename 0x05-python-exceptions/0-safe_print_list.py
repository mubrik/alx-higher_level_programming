#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    """Write a function that prints x elements of a list."""
    count = 0
    if not my_list or not x:
        return count
    for index, item in enumerate(my_list):
        if index >= x:
            break
        try:
            print(item, end="")
            count += 1
        except Exception:
            pass
    print()
    return count
