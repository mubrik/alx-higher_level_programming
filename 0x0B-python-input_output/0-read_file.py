#!/usr/bin/python3
""" Read File """


def read_file(filename=""):
    """ reads a file and prints to stdout """
    try:
        with open(filename, "r", encoding="utf-8") as f:
            print(f.read(), end="")
    except OSError as e:
        print("File cant be opened")
