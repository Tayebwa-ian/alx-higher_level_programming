#!/usr/bin/python3
"""make a JSON rep of an object"""
import json


def to_json_string(my_obj):
    """make JSON rep og a given object
    Parama:
      my_obj: the object to jsonify
    Return: NULL
    """
    return json.dumps(my_obj)
