# -*- coding: utf-8 -*-

from .coordinates import Coordinates

BOTTOM_LEFT_CORNER = Coordinates(0, 0)


class Lawn:
    """
    Lawn class
    ==========
    This class represent a lawn surface

    To simplify the navigation, the surface is a grid

    Args:
         upper_right_corner: Tuple[int, int]
            coordinates (x, y) of the cell from the upper right corner of the grid

    Attributes:
        dimensions: Tule[Coordinates, Coordinates]
            dimensions of the grid
        mowers: list[Mower]
            collection of mowers

    Methodes:
        TODO
    """

    def __init__(self, upper_right_corner: Coordinates):
        self.dimensions = (BOTTOM_LEFT_CORNER, upper_right_corner)
        self.mowers: list = list()

    def is_available_coordinates(self, coordinates: Coordinates) -> bool:
        """
        TODO
        """
        return coordinates not in [m.coordinates for m in self.mowers]

    def is_valid_coordinates(self, coordinates: Coordinates) -> bool:
        """
        TODO
        """
        return BOTTOM_LEFT_CORNER <= coordinates <= self.dimensions[1]
