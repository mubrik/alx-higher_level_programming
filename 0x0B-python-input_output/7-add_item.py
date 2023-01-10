#!/usr/bin/python3
""" Working with Files and JSON """
import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


def on_lod():
    """ store input args in JSON obj """
    try:
        # get obj
        arr = load_from_json_file("add_item.json")
    except FileNotFoundError as e:
        arr = []
    finally:
        for i, arg in enumerate(sys.argv):
            if i == 0:
                continue
            arr.append(arg)
        # save array
        save_to_json_file(arr, "add_item.json")


if __name__ == "__main__":
    on_lod()
