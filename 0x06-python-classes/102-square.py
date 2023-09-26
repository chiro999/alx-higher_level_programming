#!/usr/bin/python3

class Square:
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int and type(value) is not float:
            raise TypeError('size must be a number')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        return self.__size**2

    def __lt__(self, other):
        return self.size < other.size

    def __le__(self, other):
        return self.size <= other.size

    def __eq__(self, other):
        return self.size == other.size

    def __ne__(self, other):
        return self.size != other.size

    def __ge__(self, other):
        return self.size >= other.size
