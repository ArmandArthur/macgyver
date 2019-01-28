#! /usr/bin/env python3
# coding: utf-8

import logging as lg

import grid
import character

lg.basicConfig(level=lg.DEBUG)

def main():
    grid_texte = grid.loading('grid.txt')
    grid_transform = grid.transform(grid_texte)
    
    grid_transform_copy  = grid_transform.copy()
     
    grid_free = grid.free(grid_transform_copy)
    
    #character_tuple_position = character.create(grid_free)

    #print(character_tuple_position)
    print(grid_transform_copy)  
    #grid_transform = grid.set_position_character(character_tuple_position, grid_transform)

    #grid.draw(grid_transform)

if __name__ == '__main__':
    main()
