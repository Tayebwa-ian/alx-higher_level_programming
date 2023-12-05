#!/usr/bin/python3
"""JSON string to an object"""
import json


def from_json_string(my_str):
    """Change a json string to an object
    Params:
      my_str: the josn string
    Return: an object
    """
    return json.loads(my_str)
