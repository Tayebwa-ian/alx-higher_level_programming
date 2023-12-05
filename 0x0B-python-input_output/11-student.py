#!/usr/bin/python3
"""Student Module"""


class Student:
    """Student class to deal with student operations"""
    def __init__(self, first_name, last_name, age):
        """Class initialization method
        Params:
          first_name: first name of the student
          last_name: student's last name
          age: students's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance
        Param:
          attrs: attributes given
        Return: dictionary representation of a Student instance
        """
        if attrs is not None and all(type(i) == str for i in attrs):
            new_dict = {}
            for x in attrs:
                if x in self.__dict__.keys():
                    new_dict[x] = self.__dict__[x]
            return new_dict
        return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance
        Param:
          json: a dictionary of items to use to replace
        Return: None
        """
        for i, j in json.items():
            self.__dict__[i] = j
