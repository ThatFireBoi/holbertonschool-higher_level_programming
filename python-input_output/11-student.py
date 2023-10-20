#!/usr/bin/python3
"""Defines a class Student"""


class Student:
    """Represent a student"""

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student

        Args:
            first_name (str): The first name of the student
            last_name (str): The last name of the student
            age (int): The age of the student
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Gets a dictionary representation of the Student

        If attrs is a list of strings, only attribute names contained in this
        list must be retrieved.

        Args:
            attrs (list): A list of strings
        """
        if (type(attrs) is list and
                all(type(s) is str for s in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance

        Args:
            json (dict): A dictionary of attributes
        """
        for k, v in json.items():
            setattr(self, k, v)
