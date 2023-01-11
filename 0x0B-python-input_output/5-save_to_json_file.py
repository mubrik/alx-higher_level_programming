#!/usr/bin/python3
""" Working with Files and JSON """
import json


def save_to_json_file(my_obj, filename):
    """ save obj JSON to file """
    char_w = 0
    with open(filename, "w", encoding="utf-8") as f:
        char_w = f.write(json.dumps(my_obj))
    return char_w
