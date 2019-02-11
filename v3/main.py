#! /usr/bin/env python3
# coding: utf-8

from grid import Grid
from character import Character
from objet import Objet
import pygame

class Main :

    def __init__(self):
        self.setup()

    def setup(self):
        self.grid = Grid()
        grid = self.grid
        maps = grid.loading('grid.txt')

        self.character = Character()
        character = self.character

        # Mac gyver
        position_macgyver = character.create('positions.txt', 'macgyver')
        maps = grid.set_position_macgyver(position_macgyver, maps)

        # Gardien
        position_gardien = character.create('positions.txt', 'gardien')
        maps = grid.set_position_gardien(position_gardien, maps)

        self.objet = Objet()
        objet = self.objet

        # Aiguille
        position_aiguille = objet.create(maps)
        maps = grid.set_position_objet('aiguille',position_aiguille, maps)

        # Ether
        position_ether = objet.create(maps)
        maps = grid.set_position_objet('ether',position_ether, maps)

        # Autre
        position_tube = objet.create(maps)
        maps = grid.set_position_objet('tube', position_tube, maps)


        self.screen = pygame.display.init()
        self.screen = pygame.display.set_mode((300,300))
        screen = self.screen
        grid.draw(pygame, screen, maps)
        pygame.display.update()

        self.input_listener(maps)

    def input_listener(self, maps):
        grid = self.grid
        character = self.character
        screen = self.screen

        #screen = self.screen
        playing = True

        while playing:
            # checkerboard.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                elif event.type == pygame.KEYDOWN:
                    position_macgyver = grid.get_position_macgyver(maps)
                    if event.key == pygame.K_RIGHT:
                        maps = character.moove(maps, 'r', position_macgyver)
                    if event.key == pygame.K_LEFT:
                        maps = character.moove(maps, 'l', position_macgyver)
                    if event.key == pygame.K_DOWN:
                        maps = character.moove(maps, 'd', position_macgyver)
                    if event.key == pygame.K_UP:
                        maps = character.moove(maps, 'u', position_macgyver)

                # Redraw
                grid.draw(pygame, screen, maps)
                pygame.display.update()


main = Main()



