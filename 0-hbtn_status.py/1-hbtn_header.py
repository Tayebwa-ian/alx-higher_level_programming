#!/usr/bin/python3
"""
send a request to the URL and displays the value of the X-Request-Id variable
"""
import urllib.request
import sys


if __name__ == "__main__":
    req = sys.argv[1]
    with urllib.request.urlopen(req) as response:
        data = response.read()
    print(response.headers.get("X-Request-Id"))
