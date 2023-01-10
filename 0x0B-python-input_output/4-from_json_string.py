#!/usr/bin/python3
""" Working with JSON """
import json


def from_json_string(my_str):
    """ DeSerialize an object """
    return json.loads(my_str)
