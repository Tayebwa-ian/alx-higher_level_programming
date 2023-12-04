#!/usr/bin/python3
"""Check if object is a subclass of certain class"""


def inherits_from(obj, a_class):
    """ Check if object is a subclass of a given class
    Params:
      obj: object to check
      a_class: class to check against
    Return: True if object is a subclass otherwise false
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
