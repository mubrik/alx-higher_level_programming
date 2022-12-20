#!/usr/bin/python3
""" MagicClass Class """
import math
import dis


class MagicClass:
    """ Magic class """

    def __init__(self, radius):
        self.__radius = 0
        if type(radius) is int or type(radius) is float:
            self.__radius = radius
        else:
            raise TypeError("radius must be a number")

    def area(self):
        """ magic method for area """
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """ magic method for circ """
        return (2 * math.pi) * self.__radius
