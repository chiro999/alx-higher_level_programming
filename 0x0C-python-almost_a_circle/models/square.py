#!/usr/bin/python3
"""Defines a square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Create a new Square.

        Args:
            size (int): size of the new square
            x (int): x coordinate of the square
            y (int): y coordinate of the square
            id (int): identity of the new square
        """
        super().__init__(size, size, x, y, id)

        @property
