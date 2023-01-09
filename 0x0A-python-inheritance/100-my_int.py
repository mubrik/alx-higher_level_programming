#!/usr/bin/python3
""" Write a class MyInt that inherits from int
MyInt is a rebel. MyInt has == and != operators inverted
"""


class MyInt(int):
    """ not int, get it ? """
    def __eq__(self, __x: object):
        return not super().__eq__(__x)

    def __ne__(self, __x: object):
        return not super().__ne__(__x)
