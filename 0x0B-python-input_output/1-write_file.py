#!/usr/bin/python3
""" Write File """


def write_file(filename="", text=""):
    """ Write to a file, create if not exist, truncate if exist """
    try:
        char_w = 0
        with open(filename, "w", encoding="utf-8") as f:
            char_w = f.write(text)
        return char_w
    except OSError as e:
        print("File cant be opened")
