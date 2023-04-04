#!/usr/bin/python3
""" gets alx status with urllib"""
import sys
import urllib.parse
import urllib.request


def main(url, email):
    """ main script"""
    req = urllib.request.Request(
        url, data=urllib.parse.urlencode({'email': email}), method='POST')

    with urllib.request.urlopen(req) as response:
        body = response.read().decode('utf-8')
        print(body)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        url, email = sys.argv
        main(url, email)
