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

    def __eq__(self, other):
        """ magic method for eq """
        if not isinstance(other, Square):
            return NotImplemented
        return (self.__size == other.__size)

    def __lt__(self, other):
        """ magic method for lt """
        if not isinstance(other, Square):
            return NotImplemented
        return (self.__size < other.__size)

    def __le__(self, other):
        """ magic method for le """
        if not isinstance(other, Square):
            return NotImplemented
        return (self.__size <= other.__size)

    def __ge__(self, other):
        """ magic method for ge """
        if not isinstance(other, Square):
            return NotImplemented
        return (self.__size >= other.__size)

    def __ne__(self, other):
        """ magic method for ne """
        if not isinstance(other, Square):
            return NotImplemented
        return (self.__size != other.__size)

    def __gt__(self, other):
        """ magic method for gt """
        if not isinstance(other, Square):
            return NotImplemented
        return (self.__size > other.__size)

    def area(self):
        """ find area of square method """
        return pow(self.__size, 2)

    @property
    def size(self):
        """ getter method for size """
        return self.__size

    @size.setter
    def size(self, value):
        """ setter method for size """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @size.deleter
    def size(self):
        """ deleter method for size """
        del self.__size
