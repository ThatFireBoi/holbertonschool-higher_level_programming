#!/usr/bin/python3
"""
    This module will have a
    function that will print
    a text with 2 new lines after
    each of these characters:
    ". ? :"
"""


def text_indentation(text):
    """
    Function that prints a text
    with 2 new lines after each
    of the chracters above.
    First we check that what its
    passed is a str, then proceed to check and print.
    """
    if type(text) is not str:
        raise TypeError('text must be a string')
    for let in range(len(text)):
        if text[let] == '.' or text[let] == '?' or text[let] == ':':
            print(text[let])
            print()
        elif text[let] == " " and text[let - 1] in ['.', '?', ':']:
            continue
        else:
            print(text[let], end="")
