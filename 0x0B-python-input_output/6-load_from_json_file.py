#!/usr/bin/python3
""" Working with Files and JSON """
import json


def load_from_json_file(filename):
    """ load obj JSON from file """
    js_str = ""
    with open(filename, "r", encoding="utf-8") as f:
        js_str = f.read()
    return json.loads(js_str)
