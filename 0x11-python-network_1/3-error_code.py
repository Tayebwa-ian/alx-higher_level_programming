#!/usr/bin/python3
"""
Handle HttpError
"""
import urllib.request
import sys


if __name__ == "__main__":
    req = sys.argv[1]
    try:
        with urllib.request.urlopen(req) as response:
            pass
    except urllib.request.HTTPError as e:
        print(f"Error code: {e}")
