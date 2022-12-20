#!/usr/bin/python3
""" Square Class """


class Square:
    """ Square class with priv attri """

    def __init__(self, size=0, position=(0, 0), *args, **kwargs):
        """ initialization method """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        try:
            posa, posb = position
            if posa < 0 or posb < 0:
                raise Exception
        except Exception:
            # do something, incase user supplies (9,)
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

    def area(self):
        """ find area of square method """
        return pow(self.__size, 2)

    def my_print(self):
        """ print value of  """
        if self.__size == 0:
            print()
        # guaranteed to be safe
        posa, posb = self.__position
        for _ in range(posb):
            print()  # new line
        for _ in range(self.__size):
            if posa and not posb:
                print(" " * posa, end="")
            print("#" * self.__size)

    @property
    def size(self):
        """ getter method for size """
        return self.__size

    @property
    def position(self):
        """ getter method for position """
        return self.__position

    @size.setter
    def size(self, value):
        """ setter method for size """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @size.deleter
    def size(self):
        """ deleter method for size """
        del self.__size

    @position.setter
    def position(self, position):
        """ setter method for position """
        try:
            posa, posb = position
            if posa < 0 or posb < 0:
                raise Exception
        except Exception:
            # do something, incase user supplies (9,)
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    @position.deleter
    def position(self):
        """ deleter method for position """
        del self.__position
