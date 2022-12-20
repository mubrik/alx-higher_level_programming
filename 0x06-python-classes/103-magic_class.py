#!/usr/bin/python3
""" MagicClass Class """
import dis
import math


class MagicClass:
    """ Magic class """

    def __init__(self, radius):
        if type(radius) is not int or type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        return (2 * math.pi) * self.__radius


dis.dis(MagicClass)
