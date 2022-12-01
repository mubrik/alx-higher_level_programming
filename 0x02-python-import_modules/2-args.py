#!/usr/bin/python3
import sys


def main():
    argc = len(sys.argv)
    s = "argument"
    if argc == 1 or argc > 2:
        s = "arguments"
    print("{:d} {}{}".format(argc - 1, s, "." if argc == 1 else ":"))
    for i, arg in enumerate(sys.argv):
        if i == 0:
            continue
        print("{:d}: {}".format(i, arg))


if __name__ == "__main__":
    main()
