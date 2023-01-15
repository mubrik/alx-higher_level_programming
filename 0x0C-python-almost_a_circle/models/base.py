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
            if not type(id) == int:
                raise ValueError("id must be an integer")
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def __del__(self):
        """ delete handler, added for ease testing"""
        # decrement count
        if Base.__nb_objects:
            Base.__nb_objects = Base.__nb_objects - 1

    def update(self):
        """ Base class cant do this """
        raise NotImplementedError

    @staticmethod
    def to_json_string(list_dictionaries):
        """ json string representation """
        if not list_dictionaries:
            return "[]"
        if not isinstance(list_dictionaries, list):
            raise TypeError("Argument must be a list")
        if not all(map(lambda x: isinstance(x, dict), list_dictionaries)):
            raise TypeError("List must only contain dictionary instances")
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """ deserialize json string """
        if not json_string:
            raise TypeError("Valid string only")
        # using a try to keep method safe, remove later
        try:
            res = json.loads(json_string)
            return res
        except Exception as e:
            # except json.JSONDecodeError as e:
            # re raising so i can test easily later
            raise TypeError("Bad JSON string")

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ draw gui """
        display = Display()
        # create a method to check instances later
        if list_rectangles and isinstance(list_rectangles, list):
            display.draw_rect(list_rectangles)
        if list_squares and isinstance(list_squares, list):
            display.draw_rect(list_squares)
        display.keep_on()

    @classmethod
    def list_is_class_instance(cls, list_ins):
        """checks if all items in list is inst of class """
        return all(map(lambda x: isinstance(x, cls), list_ins))

    @classmethod
    def list_is_int_only(cls, list_int):
        """checks if all items in list are integers """
        return all(map(lambda x: type(x) == int, list_int))

    @classmethod
    def create(cls, *args, **dictionary):
        """ create a new instance wih attribs from dict """
        # treat base class diff
        if cls == Base:
            ins = Base()
        else:
            if not dictionary and not args:
                raise ValueError("Argument not valid")
            # create dummy. size and x for sq, wid he for rect
            ins = cls(1, 1)
            # update dummy
            if dictionary:
                # check if id is none
                if "id" in dictionary.keys() and dictionary["id"] is None:
                    dictionary["id"] = ins.id
                ins.update(**dictionary)
            else:
                # check if id is none
                if args[0] is None:
                    args = [item for item in args]
                    args[0] = ins.id
                ins.update(*args)
        return ins

    @classmethod
    def save_to_file(cls, list_objs):
        """ json to a file """
        # checks
        if cls == Base:
            raise NotImplementedError("Rectangle and Square intances only")
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
    def load_from_file(cls):
        """ load the list of inst from a file """
        if cls == Base:
            raise NotImplementedError("Rectangle and Square intances only")
        file_n = "{}.json".format(cls.__name__)
        # read file
        try:
            with open(file_n, mode="r") as f:
                json_str = f.read()
                arr = cls.from_json_string(json_str)
                if not isinstance(arr, list):
                    raise TypeError("File JSON object must be a list")
                return [cls.create(**ins) for ins in arr]
        except FileNotFoundError as e:
            # raise or return hmm?
            """ return [] """
            raise FileNotFoundError("{} not found".format(file_n))

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ save list of instances to a csv file """
        # checks
        if cls == Base:
            raise NotImplementedError("Rectangle and Square intances only")
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
        if cls == Base:
            raise NotImplementedError("Rectangle and Square intances only")
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
            """ return [] """
            raise FileNotFoundError("{} not found".format(file_n))
