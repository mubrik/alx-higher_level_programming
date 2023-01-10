#!/usr/bin/python3
""" Write File """


def append_after(filename="", search_string="", new_string=""):
    """ apend after a search str """
    if not filename or not isinstance(filename, str):
        return
    if not isinstance(search_string, str) or not isinstance(new_string, str):
        return
    new_str = []
    with open(filename, "r", encoding="utf-8") as f:
        # get line and add each to list list
        for line in f:
            new_str.append(line)
            if line.find(search_string) >= 0:
                new_str.append(new_string)
    # truncate and fill
    with open(filename, "w", encoding="utf-8") as f:
        f.write("".join(new_str))
