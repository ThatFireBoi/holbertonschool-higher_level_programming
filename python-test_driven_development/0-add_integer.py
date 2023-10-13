#!/usr/bin/python3
"""Module that adds 2 integers."""


def add_integer(a, b=98):
    """Function that adds 2 integers.
    Args:
        a (int): first integer
        b (int): second integer
    Returns:
        The addition of the two integers.
    Raises:
        TypeError: If a or b are not integers or floats.
    """
    if a != a:
        raise ValueError("a cannot be NaN")
    if b != b:
        raise ValueError("b cannot be NaN")
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
