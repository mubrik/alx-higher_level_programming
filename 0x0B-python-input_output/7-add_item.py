#!/usr/bin/python3
""" Working with Files and JSON  """
import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


def main():
    """ store input args in JSON obj """
    # make sure file exists
    try:
        with open("add_item.json", "x", encoding="utf-8"):
            pass
    except FileExistsError as e:
        pass
    finally:
        # file exist, make sure line valid json ob
        with open("add_item.json", "r+") as f:
            if len(f.readline()) == 0:
                f.write('[]')
        # file exist, contains valid json
        if len(sys.argv) == 1:
            return
        # get obj
        arr = load_from_json_file("add_item.json")
        for i, arg in enumerate(sys.argv):
            if i == 0:
                continue
            arr.append(arg)
        # save array
        save_to_json_file(arr, "add_item.json")


if __name__ == "__main__":
    main()
