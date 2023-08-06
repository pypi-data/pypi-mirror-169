# -*- coding: utf-8 -*-

class Coordinates:
    """
    This class represent coordinates points
    """

    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y

    def __eq__(self, other): 
        if not isinstance(other, Coordinates):
            return NotImplemented

        return self.x == other.x and self.y == other.y

    def __le__(self, other):
        if not isinstance(other, Coordinates):
            return NotImplemented

        return self.x <= other.x and self.y <= other.y

    def __str__(self):
        return f"{self.x} {self.y}"