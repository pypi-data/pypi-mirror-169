# -*- coding: utf-8 -*-

CARDINAL_POINTS = ["N", "E", "S", "W"]

class Orientation:
    """
    This class represent the orientation
    Args:
        cardinal_letter: str
            corresponding to the upper letter of the cardinal point
            => accepted values : N, E, S, W
    """

    def __init__(self, cardinal_letter: str):
        if cardinal_letter.upper() not in CARDINAL_POINTS:
            print("====", cardinal_letter)
            raise ValueError("Not a cardinal point, accepted values => N, E, S, W")
        self._current = cardinal_letter

    def rotate_right(self):
        """
        TODO
        """
        self._current = CARDINAL_POINTS[(CARDINAL_POINTS.index(self._current) + 1) % 4]

    def rotate_left(self):
        """
        TODO
        """
        self._current = CARDINAL_POINTS[(CARDINAL_POINTS.index(self._current) - 1) % 4]

    def is_north(self) -> bool:
        """
        return True if the current orientation is the north
        """
        return self._current == "N"

    def is_east(self) -> bool:
        """
        return True if the current orientation is the east
        """
        return self._current == "E"

    def is_south(self) -> bool:
        """
        return True if the current orientation is the south
        """
        return self._current == "S"

    def is_west(self) -> bool:
        """
        return True if the current orientation is the west
        """
        return self._current == "W"

    def __str__(self):
        return self._current
