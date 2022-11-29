#!/usr/bin/python3

def islower(c):
    return (ord(c) >= 97 and ord(c) <= 122)


def uppercase(str):
    for c in str:
        txt = ord(c) - 32 if islower(c) else ord(c)
        print("{:c}".format(txt), end="")
    print()  # new line
