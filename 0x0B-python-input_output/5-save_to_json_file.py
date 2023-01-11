#!/usr/bin/python3
""" Working with Files and JSON """
import json
write_file = __import__("1-write_file").write_file


def save_to_json_file(my_obj, filename):
    """ save obj JSON to file """
    return write_file(filename, json.dumps(my_obj))
