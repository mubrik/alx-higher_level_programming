#!/usr/bin/python3
""" gets alx status with urllib"""
import sys
import requests


def main(letter):
    """ main script"""
    response = requests.post(
        "http://0.0.0.0:5000/search_user", data={"q": letter})
    try:
        json = response.json()
        if json:
            print(f"[{json.get('id')}] {json.get('name')}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        main("")
