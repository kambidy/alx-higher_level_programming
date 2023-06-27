#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        if isinstance(size, int):
            self.__size = size
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        return self.__size ** 2
