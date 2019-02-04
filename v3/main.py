#! /usr/bin/env python3
# coding: utf-8

import grid
import character
import objet

def main():
    maps = grid.loading('grid.txt')
    
    # Mac gyver
    position_tuple = character.create(maps)
    maps = grid.set_position_macgyver(position_tuple, maps)

    # Gardien
    position_gardien = character.create(maps)
    maps = grid.set_position_gardien(position_gardien, maps)


    # Aiguille
    position_aiguille = objet.create(maps)
    maps = grid.set_position_objet(position_aiguille, maps)

    # Ether
    position_ether = objet.create(maps)
    maps = grid.set_position_objet(position_ether, maps)

    # Autre
    position_ether2 = objet.create(maps)
    maps = grid.set_position_objet(position_ether2, maps)

    grid.draw(maps)
    input_writing(maps)

def input_writing(maps):
    direction = input('Entrez une direction (l,r,u,d) : ')
    if direction in ['l', 'r', 'd', 'u']:
        if(direction == 'l'):
            position_macgyver = grid.get_position_macgyver(maps)
            maps = character.moove(maps,'l',position_macgyver)
        elif(direction == 'r'):
            position_macgyver = grid.get_position_macgyver(maps)
            maps = character.moove(maps,'r',position_macgyver)
        elif(direction == 'u'):
            position_macgyver = grid.get_position_macgyver(maps)
            maps = character.moove(maps,'u',position_macgyver)
        elif(direction == 'd'):
            position_macgyver = grid.get_position_macgyver(maps)
            maps = character.moove(maps,'d',position_macgyver)
        grid.draw(maps)
        input_writing(maps)   
        

if __name__ == '__main__':
    main()

r
