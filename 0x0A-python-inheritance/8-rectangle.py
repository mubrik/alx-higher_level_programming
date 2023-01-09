#!/usr/bin/python3
""" BaseGeometry Class """


class BaseGeometry:
    """ BaseGeometry class """

    def area(self):
        """ area of geometry """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validate value """
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        return value


class Rectangle(BaseGeometry):

    def __init__(self, width, height):
        """ init method """
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)