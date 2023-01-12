#!/usr/bin/python3
""" Square Class  """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ the Square base """

    def __init__(self, size, x=0, y=0, id=None):
        """ init method """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ string representation """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.__width)

    @property
    def size(self):
        """ size getter """
        return self.__width

    @size.setter
    def size(self, value):
        """ size property setter """
        self.__width = super().validate_len("width", value)
        self.__height = super().validate_len("height", value)

    def update(self, *args, **kwargs):
        """ update the instance """
        arg_l = ["id", "size", "x", "y"]
        if args and isinstance(args, (list, tuple)):
            for i, value in enumerate(args):
                # validate?
                name = arg_l[i]
                self.__upd_or_raise(name, value)
        elif kwargs:
            for key, value in kwargs.items():
                self.__upd_or_raise(key, value)

    def __upd_or_raise(self, name, value):
        """ helper for update method """
        arg_l = ["id", "size", "x", "y"]
        if name == arg_l[0] and self.ty_int(name, value):
            self.id = value
        elif name == arg_l[1]:
            setattr(self, name, self.validate_len(name, value))
        elif name in arg_l[2:]:
            setattr(self, name, self.validate_pos(name, value))
