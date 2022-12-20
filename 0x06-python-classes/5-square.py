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

    def area(self):
        """ find area of square method """
        return pow(self.__size, 2)

    def my_print(self):
        """ print value of  """
        if self.__size == 0:
            print()
        for _ in range(self.__size):
            print("#" * self.__size)

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
