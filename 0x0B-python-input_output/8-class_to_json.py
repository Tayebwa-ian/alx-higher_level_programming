#!/usr/bin/python3
"""Dictionary for JSON serialization of an object"""


def class_to_json(obj):
    """serialization of class object
    Params:
      obj: the class object
    Return: dictionary description with simple data structure
    """
    return obj.__dict__
