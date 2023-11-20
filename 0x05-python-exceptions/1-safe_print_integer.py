#!/usr/bin/python3

def safe_print_integer(value):
    """
    Description: prints integers
    Params:
     -value: any datatype
    Return: True if it print the integer otherwise false
    """
    try:
        print("{:d}".format(value))
        return True
    except ValueError:
        return False
