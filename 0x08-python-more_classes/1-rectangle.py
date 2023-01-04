#!/usr/bin/python3
""" Rectangle Class """


class Rectangle:
    """ Rectangle class with priv attri """

    def __init__(self, width=0, height=0, *args, **kwargs):
        """ initialization method, checks handled by setters """
        self.height = height
        self.width = width

    @property
    def width(self):
        """ rect width """
        return self.__width

    @property
    def height(self):
        """ rect height """
        return self.__height

    @width.setter
    def width(self, value):
        """ rect width setter """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """ rect height setter """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
