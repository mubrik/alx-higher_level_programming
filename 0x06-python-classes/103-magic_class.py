#!/usr/bin/python3
""" MagicClass Class """
import math


class MagicClass:
    """ Magic class """

    def __init__(self, radius):
        """ magic method for init """
        self.__radius = 0
        if type(radius) != int and type(radius) != float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """ method for area """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """ method for circumference """
        return 2 * math.pi * self.__radius
