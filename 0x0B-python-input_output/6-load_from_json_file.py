#!/usr/bin/python3
"""creates an Object from a JSON file"""
import json


def load_from_json_file(filename):
    """ creates an Object from a “JSON file
    Param:
      filename: the filename to read from
    Return: the object created
    """
    with open(filename, 'r', encoding="UTF8") as f:
        return json.load(f)
