#!/usr/bin/python3
""" Square Class  """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ the Square base """
    _keys = ["id", "size", "x", "y"]

    def __init__(self, size, x=0, y=0, id=None):
        """ init method """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ string representation """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """ size getter """
        return self.width

    @size.setter
    def size(self, value):
        """ size property setter """
        self.width = super().validate_len("width", value)
        self.height = super().validate_len("height", value)

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
        # validate, update or raise
        if key == self._keys[0] and self.ty_int(key, value):
            self.id = value
        elif key == self._keys[1]:
            self.size = value
        elif key in self._keys[2:]:
            setattr(self, key, self.validate_pos(key, value))

    def to_dictionary(self):
        """ dict representation """
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y,
        }
