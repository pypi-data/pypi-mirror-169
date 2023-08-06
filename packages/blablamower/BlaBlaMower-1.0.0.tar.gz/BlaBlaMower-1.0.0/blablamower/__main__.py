# -*- coding: utf-8 -*-

import sys
from threading import Thread

from .core import Config, Lawn, Mower


def wait_all_mowers(mowing_list: "list[Thread]"):
    """
    Wait for all mowers to finish mowing
    """
    for thread in mowing_list:
        thread.join()
    mowing_list.clear()


def start(file_path):
    """
    TODO
    """
    config = Config(file_path)
    lawn = Lawn(config.upper_right_corner)
    for mower in config.mower_list:
        lawn.mowers.append(Mower(lawn, mower[0], mower[1], mower[2]))

    mowing_list: list[Thread] = []
    for mower in lawn.mowers:
        mowing = Thread(target=mower.start_mowing)
        mowing_list.append(mowing)
        mowing.start()
    wait_all_mowers(mowing_list)
    for mower in lawn.mowers:
        print(mower)


def main():
    if len(sys.argv) == 1:
        print("You must provide an input file !")
    else:
        start(sys.argv[1])


if __name__ == "__main__":
    main()
