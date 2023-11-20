#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
    except Exception as er:
        print("Exception: {}".format(er), file = sys.stderr)
        result = None
    return result
