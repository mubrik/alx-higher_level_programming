#!/usr/bin/python3
""" gets alx status with urllib"""
import sys
import requests
import requests.exceptions


def main(url):
    """ main script"""
    response = requests.get(url)
    if response.status_code >= 400:
        print(f'Error code: {response.status_code}')
    else:
        print(response.text)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        _, url = sys.argv
        main(url)
