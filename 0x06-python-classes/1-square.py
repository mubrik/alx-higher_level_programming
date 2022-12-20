#!/usr/bin/python3
""" Square Class """


class Square:
    """ Square class with priv attri """

    def __init__(self, size, *args, **kwargs):
        """ initialization method """
        self.__size = size
