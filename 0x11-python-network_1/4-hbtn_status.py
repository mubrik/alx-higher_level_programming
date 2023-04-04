#!/usr/bin/python3
""" gets alx status with requests"""
import requests


def main(url):
    """ main script"""
    response = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))


if __name__ == "__main__":
    main("https://alx-intranet.hbtn.io/status")
