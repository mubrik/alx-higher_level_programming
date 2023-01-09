#!/usr/bin/python3
""" Rectangle Class """


class BaseGeometry:
    """ Main BaseGeometry class """

    def area(self):
        """ area of geometry """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validate value to be an int """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        return value


class Rectangle(BaseGeometry):
    """ Rectangle class """

    def __init__(self, width, height):
        """ init method """
        self.__height = super().integer_validator("height", height)
        self.__width = super().integer_validator("width", width)
