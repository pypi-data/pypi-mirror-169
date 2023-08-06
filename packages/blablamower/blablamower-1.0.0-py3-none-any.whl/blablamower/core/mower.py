# -*- coding: utf-8 -*-

from copy import deepcopy
from time import sleep

from .coordinates import Coordinates
from .lawn import Lawn
from .orientation import Orientation


class Mower:
    """
    This class contain the coordinates and the orientation of a mower.
    A mower is able to turn left, turn right and go forward
    Args:
        coordinates: Coordinates
            coordinates of the mower on the lawn
        orientation: str
            letter corresponding to one of the 4 cardinal points (N, E, S, W)
    Attributes:
        coordinates: Coordinates
            coordinates of the mower on the lawn
        orientation: Orientation
            orientation of the mower, a letter corresponding to one of the 4 cardinal points (N, E, S, W)
    """

    def __init__(
        self,
        lawn: Lawn,
        coordinates: Coordinates,
        orientation: Orientation,
        instructions: "list[str]",
    ):
        self.uid: str = f"{coordinates}{orientation}".replace(" ", "")
        self.lawn: Lawn = lawn
        self.coordinates: Coordinates = coordinates
        self.orientation: Orientation = orientation
        self.instructions: list[str] = instructions

    def start_mowing(self):
        """
        Execute the mowing instructions
        """
        for instruction in self.instructions:
            if instruction == "L":
                self.turn_left()
            elif instruction == "R":
                self.turn_right()
            elif instruction == "F":
                self.move_forward()
            sleep(1)  # TODO move to config

    def turn_left(self):
        """
        Rotate the mower of 90° at the left
        """
        previous_orientation = deepcopy(self.orientation)
        self.orientation.rotate_left()
        print(
            f"Mower {self.uid} has turned to left (from {previous_orientation} to {self.orientation})"
        )

    def turn_right(self):
        """
        Rotate the mower of 90° at the right
        """
        previous_orientation = deepcopy(self.orientation)
        self.orientation.rotate_right()
        print(
            f"Mower {self.uid} has turned to right (from {previous_orientation} to {self.orientation})"
        )

    def move_forward(self):
        """
        Move forward the mower
        """
        new_coordinates = deepcopy(self.coordinates)
        if self.orientation.is_north():
            new_coordinates.y += 1
        elif self.orientation.is_east():
            new_coordinates.x += 1
        elif self.orientation.is_south():
            new_coordinates.y -= 1
        elif self.orientation.is_west():
            new_coordinates.x -= 1
        if self.lawn.is_valid_coordinates(new_coordinates):
            if self.lawn.is_available_coordinates(new_coordinates):
                self.coordinates = deepcopy(new_coordinates)
                print(
                    f"Mower {self.uid} has moved forward in the direction of the cardinal point {self.orientation} (new coordinates :{self.coordinates})"
                )
            else:
                print(
                    f"Mower {self.uid} the new coordinates are bussy, the instructions are ingored"
                )
        else:
            print(
                f"Mower {self.uid} the new coordinates are outside of the lawn, the instructions are ingored"
            )

    def __str__(self) -> str:
        """
        Return a string corresponding to position of the mower,
        """
        return f"{self.coordinates} {self.orientation}"
