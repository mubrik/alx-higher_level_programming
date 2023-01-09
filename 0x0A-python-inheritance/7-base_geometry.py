#!/usr/bin/python3
""" BaseGeometry Class """


class BaseGeometry:
    """ Main BaseGeometry class """

    def area(self):
        """ area of geometry """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validate value to be an int """
        """ if not isinstance(name, str):
            raise TypeError("name must be a string") """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
