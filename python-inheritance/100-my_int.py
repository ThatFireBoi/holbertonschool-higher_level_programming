#!/usr/bin/python3
"""Defines a class MyInt that inherits from int"""


class MyInt(int):
    """MyInt class"""

    def __eq__(self, other):
        """Override == operator with != behavior"""
        return super().__neg__(other)

    def __neg__(self, other):
        """Override != operator with == behavior"""
        return super().__eq__(other)
