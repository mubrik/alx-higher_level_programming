#!/usr/bin/python3
""" gets alx status with requests"""
import sys
import requests


def main(url):
    """ main script"""
    response = requests.get(url)
    print(response.headers.get('X-Request-Id'))


if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv[1])
