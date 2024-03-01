#!/usr/bin/python3
"""
post request
"""
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    values = {'email': email}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        result = response.read()
    print(f"Your email is: {result.decode('ascii')}")
