#!/usr/bin/python3
"""This module creates a class named square"""


class Square:
    """class Square that defines a square"""

    def __init__(self, size=0):
        """Instantiation"""
        self.__size = size
        if type(size) is not int:  # check if size not an integer
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >=0")
