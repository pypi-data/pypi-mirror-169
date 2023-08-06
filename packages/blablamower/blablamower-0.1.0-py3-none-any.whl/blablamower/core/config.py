# -*- coding: utf-8 -*-

from typing import Tuple

from .coordinates import Coordinates
from .orientation import Orientation


class Config:
    def __init__(self, file_path: str) -> None:
        # TODO check if file existe
        self.lignes: list[str] = self.__parse_file__(file_path)
        self.upper_right_corner: Coordinates = self.__get_upper_right_corner__()
        self.mower_list: list[Tuple(Coordinates, Orientation, Tuple[str])] = []
        self.__parse_mower_list__()
        pass

    def __parse_file__(self, file_path: str):
        with open(file_path, "r") as f:
            return f.read().splitlines()

    def __get_upper_right_corner__(self) -> Tuple[int, int]:
        first_line_data = self.lignes.pop(0).split(" ")
        # TODO check data
        return Coordinates(int(first_line_data[0]), int(first_line_data[1]))

    def __parse_mower_list__(self) -> None:
        for a, b in zip(*[iter(self.lignes)] * 2):
            coordinates = self.__parse_mower_coordinates__(a)
            orientation = self.__parse_mower_orientation__(a)
            instructions = self.__parse_mower_instructions__(b)
            self.mower_list.append((coordinates, orientation, instructions))
        return

    def __parse_mower_coordinates__(self, position: str) -> Coordinates:
        return Coordinates(int(position.split(" ")[0]), int(position.split(" ")[1]))

    def __parse_mower_orientation__(self, position: str) -> Orientation:
        return Orientation(position.split(" ")[2])

    def __parse_mower_instructions__(self, instructions: str) -> Tuple[str]:
        return tuple(instructions)
