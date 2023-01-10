#!/usr/bin/python3
""" Square Class """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square Class """

    def __init__(self, size):
        """ init method """
        super().integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """ find area of square method """
        return super().area()

    def __str__(self):
        """ string representation """
        return super().__str__().replace("Rectangle", "Square")
