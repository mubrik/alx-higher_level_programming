#!/usr/bin/python3
""" gets alx status with urllib"""
import sys
import urllib.request


def main(url):
    """ main script"""
    with urllib.request.urlopen(url) as response:
        print(response.headers.get("X-Request-Id"))


if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
