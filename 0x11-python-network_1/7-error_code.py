#!/usr/bin/python3
""" gets alx status with urllib"""
import sys
import requests
import requests.exceptions


def main(url):
    """ main script"""
    try:
        response = requests.get(url)
        print(response.text)
    except requests.exceptions.HTTPError as exc:
        print(f'Error code: {exc.errno}')


if __name__ == "__main__":
    if len(sys.argv) == 2:
        _, url = sys.argv
        main(url)
