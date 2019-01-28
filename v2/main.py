#! /usr/bin/env python3
# coding: utf-8

import logging as lg

import grid

lg.basicConfig(level=lg.DEBUG)

def main():
    grid_texte = grid.loading('grid.txt')
    grid_transform = grid.transform(grid_texte)
    grid_draw = grid.draw(grid_transform)

    #print(grid_draw)

if __name__ == '__main__':
    main()
