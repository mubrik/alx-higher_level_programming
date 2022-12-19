#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    """Write a function that prints the first x elements of a list and only
        integers."""
    count = 0
    if not my_list:
        print()
        return count
    for index in range(x):
        if not isinstance(my_list[index], int):
            continue
        try:
            print("{:d}".format(my_list[index]), end="")
            count += 1
        except Exception:
            pass
    print()  # newline
    return count
