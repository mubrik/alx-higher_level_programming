#!/usr/bin/python3


def uniq_add(my_list: list = []):
    """ add unique items in list """
    if not my_list:
        return my_list
    # use set for unique
    uniq = set(my_list)
    total = 0
    for num in uniq:
        total += num
    return total
