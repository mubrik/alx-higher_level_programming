#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    if not my_list:
        return my_list
    return [True if x % 2 == 0 else False for x in my_list]
