#!/usr/bin/python3
""" gets alx status with urllib"""
import sys
import urllib.error
import urllib.request


def main(url):
    """ main script"""
    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        print(f'Error code: {exc.code}')


if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
