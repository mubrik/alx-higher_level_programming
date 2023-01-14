#!/usr/bin/python3
""" Base Class  """
import json
import csv
from .graphics import Display


class Base:
    """ base class for this module """
    __nb_objects = 0

    def __init__(self, id=None):
        """ init method """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ json string representation """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """ deserialize json string """
        if not json_string:
            return []
        # using a try to keep method safe, remove later
        try:
            res = json.loads(json_string)
            return res
        except Exception:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        display = Display()
        # create a method to check instances later
        if list_rectangles and isinstance(list_rectangles, list):
            display.draw_rect(list_rectangles)
        if list_squares and isinstance(list_squares, list):
            display.draw_rect(list_squares)
        display.keep_on()

    @classmethod
    def is_class(cls, ins):
        """ is instance wrapper """
        return isinstance(ins, cls)

    @classmethod
    def list_is_class_instance(cls, list_ins):
        """checks if all items in list is inst of class """
        return all(map(lambda x: isinstance(x, cls), list_ins))

    @classmethod
    def save_to_file(cls, list_objs):
        """ json to a file """
        # checks
        if not list_objs or not isinstance(list_objs, list):
            list_objs = []
        if not cls.list_is_class_instance(list_objs):
            raise TypeError(
                "List must contain only instances of {}".format(cls.__name__)
            )
        file_n = "{}.json".format(cls.__name__)
        # map each instance to its dict
        list_objs = list(map(lambda x: x.to_dictionary(), list_objs))
        # open file, truncate if exist
        with open(file_n, mode="w") as f:
            f.write(cls.to_json_string(list_objs))

    @classmethod
    def create(cls, *args, **dictionary):
        """ create a new instance wih attribs from dict """
        if not dictionary and not args:
            return
        # create dummy. size and x for sq, wid he for rect
        ins = cls(1, 1)
        # update dummy
        if dictionary:
            ins.update(**dictionary)
        else:
            ins.update(*args)
        return ins

    @classmethod
    def load_from_file(cls):
        """ load the list of inst from a file """
        file_n = "{}.json".format(cls.__name__)
        # read file
        try:
            with open(file_n, mode="r") as f:
                json_str = f.read()
                # safe call
                arr = cls.from_json_string(json_str)
                return [cls.create(**ins) for ins in arr]
        except FileNotFoundError as e:
            # raise or return hmm?
            """ raise FileNotFoundError("{} not found".format(file_n)) """
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ save list of instances to a csv file """
        # checks
        if not list_objs or not isinstance(list_objs, list):
            list_objs = []
        if not cls.list_is_class_instance(list_objs):
            raise TypeError(
                "List must contain only instances of {}".format(cls.__name__)
            )
        file_n = "{}.csv".format(cls.__name__)
        # map each instance to its dict
        list_objs = list(map(lambda x: x.to_dictionary(), list_objs))
        # write to a csv file
        with open(file_n, mode="w", newline="") as csv_f:
            csv_write = csv.DictWriter(csv_f, cls._keys)
            csv_write.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        file_n = "{}.csv".format(cls.__name__)
        # read file
        try:
            with open(file_n, mode="r", newline="") as csv_f:
                arr = []
                try:
                    for row in csv.reader(csv_f):
                        arr.append([int(s) for s in row])
                except Exception as e:
                    raise TypeError("Bad CSV file")
                return [cls.create(*ins) for ins in arr]
        except FileNotFoundError as e:
            # raise or return hmm?
            """ raise FileNotFoundError("{} not found".format(file_n)) """
            return []
