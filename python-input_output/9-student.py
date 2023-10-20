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

        Raises:
            TypeError: If first_name is not a string
            TypeError: If last_name is not a string
            TypeError: If age is not a integer
            ValueError: If age is less than 0
        """
        if type(first_name) is not str:
            raise TypeError("first_name must be a string")
        if type(last_name) is not str:
            raise TypeError("last_name must be a string")
        if type(age) is not int:
            raise TypeError("age must be an integer")
        if age < 0:
            raise ValueError("age must be greater than or equal to 0")

        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age

    def to_json(self):
        """Gets a dictionary representation of the Student

        Returns:
            dict: A dictionary representation of the Student
        """
        return self.__dict__
