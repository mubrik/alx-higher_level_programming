#!/usr/bin/python3
""" Working with Files and JSON """


class Student:
    """ class holding student data """

    def __init__(self, first_name, last_name, age):
        """ init method """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        ret_d = vars(self)
        if attrs is None or not attrs:
            return ret_d
        if type(attrs) is list and all(map(lambda x: type(x) is str, attrs)):
            n_dict = {}
            for key in filter(lambda k: k in ret_d.keys(), attrs):
                n_dict[key] = ret_d[key]
            return n_dict

    def reload_from_json(self, json):
        for key, value in json.items():
            if key in vars(self):
                setattr(self, key, value)
