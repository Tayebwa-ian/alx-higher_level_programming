#!/usr/bin/python3
"""Dictionary for JSON serialization of an object"""
to_json_string = __import__('3-to_json_string').to_json_string


def class_to_json(obj):
    """serialization of class object
    Params:
      obj: the class object
    Return: dictionary description with simple data structure
    """
    return to_json_string(obj.__dict__)
