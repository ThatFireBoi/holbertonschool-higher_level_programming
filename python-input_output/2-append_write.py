#!/usr/bin/python3
"""Defines a function that appends a string to a text file"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file (UTF8)
    and returns # of chars written.
    """
    with open(filename, "a", encoding='utf-8') as f:
        return f.write(text)
