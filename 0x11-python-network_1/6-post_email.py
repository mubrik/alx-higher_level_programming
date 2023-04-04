#!/usr/bin/python3
""" gets alx status with urllib"""
import sys
import requests


def main(url, email):
    """ main script"""
    response = requests.post(url, data={'email': email})
    print(response.text)


if __name__ == "__main__":
    if len(sys.argv) == 3:
        _, url, email = sys.argv
        main(url, email)
