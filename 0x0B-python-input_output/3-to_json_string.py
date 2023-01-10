#!/usr/bin/python3
""" Working with JSON """
import json


def to_json_string(my_obj):
    """ Serialize an object """
    return json.dumps(my_obj)
