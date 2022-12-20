#!/usr/bin/python3
""" Square Class """


class Square:
    """ Square class with priv attri """

    def __init__(self, size=0, *args, **kwargs):
        """ initialization method """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        pass
