#!/usr/bin/python3
"""Defines a class MyInt that inherits from int"""


class MyInt(int):
    """MyInt class"""

    def __eq__(self, other):
        """Override == operator with != behavior"""
        return self.real != other

    def __neg__(self, other):
        """Override != operator with == behavior"""
        return self.real == other
