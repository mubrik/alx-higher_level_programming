#!/usr/bin/python3
""" gets alx status with urllib"""
import urllib.request


def main(url):
    """ main script"""
    with urllib.request.urlopen(url) as response:
        content = response.read()

    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))
    print("\t- utf8 content: {}".format(content.decode("utf-8")))


if __name__ == '__main__':
    main("https://alx-intranet.hbtn.io/status")
