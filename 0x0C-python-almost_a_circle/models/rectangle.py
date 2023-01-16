#!/usr/bin/python3
""" Rectangle Class  """
from models.base import Base


class Rectangle(Base):
    """ the rectangle base """
    _keys = ["id", "width", "height", "x", "y"]

    def __init__(self, width, height, x=0, y=0, id=None):
        """ init method """
        super().__init__(id)
        self.__width = self.validate_len("width", width)
        self.__height = self.validate_len("height", height)
        self.__x = self.validate_pos("x", x)
        self.__y = self.validate_pos("y", y)

    def __str__(self):
        """ string representation  """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    @property
    def width(self):
        """ width getter """
        return self.__width

    @property
    def height(self):
        """ height getter """
        return self.__height

    @property
    def x(self):
        """ x getter """
        return self.__x

    @property
    def y(self):
        """ y getter """
        return self.__y

    @width.setter
    def width(self, value):
        """ width setter """
        self.__width = self.validate_len("width", value)

    @height.setter
    def height(self, value):
        """ height setter """
        self.__height = self.validate_len("height", value)

    @x.setter
    def x(self, value):
        """ x setter """
        self.__x = self.validate_pos("x", value)

    @y.setter
    def y(self, value):
        """ y setter """
        self.__y = self.validate_pos("y", value)

    def area(self):
        """ area of rect """
        return self.height * self.width

    def display(self):
        """ print the rectangle """
        if not self.area:
            return
        row = "{}{}\n".format(
            " " * self.x, "#" * self.width)
        # print y pos
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(row, end="")

    def ty_int(self, name, value):
        """ validate specific type """
        if not type(value) == int:
            raise TypeError("{} must be an integer".format(name))
        return True

    def gt_zero(self, name, value):
        """ greater than 0 """
        if not value > 0:
            raise ValueError("{} must be > 0".format(name))
        return True

    def ge_zero(self, name, value):
        """ greater than or equal  0 """
        if not value >= 0:
            raise ValueError("{} must be >= 0".format(name))
        return True

    def validate_len(self, name, value):
        """ validate a length value, width/height """
        if self.ty_int(name, value) and self.gt_zero(name, value):
            return value

    def validate_pos(self, name, value):
        """ validate a pos value, x/y """
        if self.ty_int(name, value) and self.ge_zero(name, value):
            return value

    def update(self, *args, **kwargs):
        """ update the instance """
        if args and isinstance(args, (list, tuple)):
            for i, value in enumerate(args):
                # not necessary but save cycle
                if i >= len(self._keys):
                    break
                key = self._keys[i]
                self._upd_or_raise(key, value)
        elif kwargs:
            for key, value in kwargs.items():
                self._upd_or_raise(key, value)

    def _upd_or_raise(self, key, value):
        """ helper for update method """
        # validate, update or raise. raise if name not in keys?
        if key == self._keys[0] and self.ty_int(key, value):
            self.id = value
        elif key in self._keys[1:3]:
            setattr(self, key, self.validate_len(key, value))
        elif key in self._keys[3:]:
            setattr(self, key, self.validate_pos(key, value))

    def to_dictionary(self):
        """ dict representation """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y,
        }
