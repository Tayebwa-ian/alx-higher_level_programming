#!/usr/bin/python3
""" Return object attributes and methods in a list"""


def lookup(obj):
    """returns the list of available attributes and methods of an object
    Param:
      obj: object to use
    Retun: list of available attributes and methods of an object
    """
    return list(dir(obj))
