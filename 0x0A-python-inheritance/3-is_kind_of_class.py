#!/usr/bin/python3
"""Function that returns True if object is instance of a given class"""


def is_kind_of_class(obj, a_class):
    """ check if object is kind of an isnatnce of a class given
    Params:
      obj: the object to check
      a_class: the class to check against
    Return: True if object is kind of an instance and false otherwise
    """
    return isinstance(obj, a_class)
