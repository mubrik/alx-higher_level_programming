#!/usr/bin/python3
import sys


def main():
    argc = len(sys.argv)
    print("{:d} argument{}".format(argc - 1, "." if argc == 1 else "s:"))
    for i, arg in enumerate(sys.argv):
        if i == 0:
            continue
        print("{:d}: {}".format(i, arg))


if __name__ == "__main__":
    main()
