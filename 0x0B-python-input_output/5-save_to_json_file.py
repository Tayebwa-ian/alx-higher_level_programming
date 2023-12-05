#!/usr/bin/python3
""" write a json rep of an object in a file"""
import json


def save_to_json_file(my_obj, filename):
    """write a json rep of an object to a file
    Params:
      my_obj: the given object
      filename: the file to write to
    Return: Number of bytes written to a file
    """
    st = json.dumps(my_obj)
    with open(filename, 'w', encoding="UTF8") as f:
        return f.write(st)
