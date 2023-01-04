#!/usr/bin/python3
""" Rectangle Class """


class Rectangle:
    """ Rectangle class with priv attri """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0, *args, **kwargs):
        """ initialization method, checks handled by setters """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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

    def area(self):
        """ rect area """
        return self.height * self.width

    def perimeter(self):
        """ rect perimeter """
        if not self.width or not self.height:
            return 0
        return 2 * (self.height + self.width)

    def __str__(self):
        """ string representation """
        new_str = ""
        if not self.area():
            return new_str
        # iterate heiggh/rows first then width/col
        for i in range(self.height):
            new_str = f"{new_str}{self.print_symbol * self.width}"
            if i != (self.height - 1):
                new_str = new_str + "\n"
        return new_str

    def __repr__(self):
        """ represational state """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """ metho called after garbage collection """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
