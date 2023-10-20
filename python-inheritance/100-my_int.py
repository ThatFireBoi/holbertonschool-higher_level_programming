#!/usr/bin/python3
"""Defines a class MyInt that inherits from int"""


class MyInt(int):
    """MyInt class"""

    def __eq__(self, value):
        """Override == operator with != behavior"""
        return self.real != value

    def __neg__(self, value):
        """Override != operator with == behavior"""
        return self.real == value
