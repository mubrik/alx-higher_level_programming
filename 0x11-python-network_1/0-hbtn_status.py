#!/usr/bin/env python3
""" gets alx status with urllib"""
import urllib.request


def run(url):
    with urllib.request.urlopen(url) as response:
        content = response.read()

    print("Body response:")
    print("    - type: {}".format(type(content)))
    print("    - content: {}".format(content))
    print("    - utf8 content: {}".format(content.decode("utf-8")))


if __name__ == '__main__':
    run("https://alx-intranet.hbtn.io/status")
