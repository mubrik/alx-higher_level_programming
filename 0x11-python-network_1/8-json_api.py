#!/usr/bin/python3
""" gets alx status with urllib"""
import sys
import urllib
import urllib.request


def main(url, email):
    """ main script"""
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    req = urllib.request.Request(url, data=data, method='POST')

    with urllib.request.urlopen(req) as response:
        body = response.read().decode('utf-8')
        print(body)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        url, email = sys.argv
        main(url, email)
