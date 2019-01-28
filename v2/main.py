#! /usr/bin/env python3
# coding: utf-8

import logging as lg

import grid
import character

lg.basicConfig(level=lg.DEBUG)

def main():
    maps = grid.loading('grid.txt')
    
    position_tuple = character.create(maps)
    maps = grid.set_position_macgyver(position_tuple, maps)
    grid.draw(maps)

if __name__ == '__main__':
    main()
