#!/usr/bin/python3
""" This is MyList module

The module supplies one class, MyList().
A class MyList that inherits from list

>>> MyList()
[...]
"""


class MyList(list):
    """ MyList that inherits from list """

    def print_sorted(self):
        """ method to print sorted list """
        print(sorted(self))
