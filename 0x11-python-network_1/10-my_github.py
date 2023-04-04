#!/usr/bin/python3
""" gets alx status with urllib"""
import sys
import requests


def main(username, password):
    """ main script"""
    endpoint = "https://api.github.com/user"
    headers = {"Accept": "application/vnd.github.v3+json"}
    auth = (username, password)

    response = requests.get(endpoint, headers=headers, auth=auth)

    if response.status_code == 200:
        json_response = response.json()
        print(json_response["id"])
    else:
        print("None")


if __name__ == "__main__":
    if len(sys.argv) == 3:
        _, username, password = sys.argv
        main(username, password)
