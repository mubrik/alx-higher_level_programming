#!/usr/bin/python3
import sys


def main():
    result = 0
    for i, arg in enumerate(sys.argv):
        if i == 0:
            continue
        result += int(arg)
    print(result)


if __name__ == "__main__":
    main()
