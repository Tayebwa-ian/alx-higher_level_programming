#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    """
    Description: prints integers
    Params:
     -value: any datatype
    Return: True if it print the integer otherwise false
    """
    try:
        print("{:d}".format(value))
        return True
    except Exception as er:
        sys.stderr.write("Exception: {}\n".format(er))
        return False
