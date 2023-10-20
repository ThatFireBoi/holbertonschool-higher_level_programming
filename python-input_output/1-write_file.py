#!/usr/bin/python3
"""Function that writes string to text file and returns # of chars written"""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) and returns # of chars written"""
    with open(filename, "w", encoding='utf-8') as f:
        return f.write(text)
