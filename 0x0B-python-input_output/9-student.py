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

    def to_json(self):
        """retrieves a dictionary representation of a Student instance"""
        return self.__dict__
