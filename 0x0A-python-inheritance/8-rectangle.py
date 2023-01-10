#!/usr/bin/python3
""" Rectangle Class """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle class """

    def __init__(self, width, height):
        """ init method """
        self.__height = super().integer_validator("height", height)
        self.__width = super().integer_validator("width", width)
