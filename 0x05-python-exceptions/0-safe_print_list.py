#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    """Write a function that prints x elements of a list."""
    count = 0
    if not my_list:
        return count
    for index in range(x):
        """ if index >= x:
            break """
        try:
            print(my_list[index], end="")
            count += 1
        except Exception:
            pass
    print()
    return count
