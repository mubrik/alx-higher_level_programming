#!/usr/bin/python3
""" Working with Files and JSON """


class Student:
    """ class holding student data """

    def __init__(self, first_name, last_name, age):
        """ init method """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ to json method """
        return vars(self)
