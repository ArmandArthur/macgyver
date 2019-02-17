#! /usr/bin/env python3
# coding: utf-8

"""
    Import, class
"""

from grid import Grid
from character import Character
from object import Object
from display import Display

class Main:
    """
        Initializing grid, character and objects
        Listening the input key
    """
    display = 0

    def __init__(self):
        """
            Run the application
        """
        self.display = Display.getInstance()
        self.setup()

    def setup(self):
        """
            Characters from maps and objects random, run pygame, listener input
        """
        grid = Grid()
        maps = grid.loading('grid.txt')

        # Mac gyver
        macgyver = Character('grid.txt', 'M')
        #self.macgyver = macgyver

        # Guardian
        #Character('grid.txt', 'G')

        # Needle
        o_n = Object(maps)
        maps = grid.set_position('needle', (o_n.position_x, o_n.position_y), maps)

        # Ether
        o_e = Object(maps)
        maps = grid.set_position('ether', (o_e.position_x, o_e.position_y), maps)

        # Tube
        o_t = Object(maps)
        maps = grid.set_position('tube', (o_t.position_x, o_t.position_y), maps)

        self.display.init_pygame(macgyver, maps, grid)
        self.display.set_text("BEGIN")

        grid.draw(maps)
        self.display.update()
        self.display.listener()



Main()
