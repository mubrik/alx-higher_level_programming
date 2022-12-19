#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    """Write a function that prints x elements of a list."""
    if not my_list:
        return
    count = 0
    for index, item in enumerate(my_list):
        if index >= x:
            break
        try:
            print(str(item), end="")
            count += 1
        except Exception:
            pass
    print()
    return count
