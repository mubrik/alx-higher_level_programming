#!/usr/bin/python3
""" Base Class  """
import json


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
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """ json to a file """
        if list_objs is None:
            list_objs = []
        file_name = "{}.json".format(cls.__name__)
        # map each instance to its dict
        list_objs = list(map(lambda x: x.to_dictionary(), list_objs))
        # open file, truncate if exist
        with open(file_name, mode="w") as f:
            f.write(cls.to_json_string(list_objs))
