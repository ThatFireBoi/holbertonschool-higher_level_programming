#!/usr/bin/python3
""" Square class """


from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initilizes the square.

        Args:
            size (int): size of the square
            x (int): x coordinate of the square
            y (int): y coordinate of the square
            id (int): id of the square
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns the string representation of the square"""
        return '[Square] ({}) {}/{} - {}'.format(self.id, self.x, self.y,
                                                 self.width)

    @property
    def size(self):
        """Returns the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the size of the square"""
        self.width = value
        self.height = value
