#!/usr/bin/python3
""" Fetch a url
"""
import urllib.request


if __name__ == "__main__":
    req = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(req) as response:
        data = response.read()
    print("Body response:")
    print("\t- type: {}".format(data.__class__))
    print("\t- content: {}".format(data))
    print("\t- utf8 content: {}".format(data.decode('ascii')))
