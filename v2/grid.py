
import os
import sys

def loading(data_file):
	
	directory = os.path.dirname(__file__)
	path_to_file = os.path.join(directory, 'data', data_file)
	
	grid = []

	with open(path_to_file) as file:
		for line in file:
			maps = []
			for character in line:
				if character != '\n':
					maps.append(character)
			grid.append(maps)
	return grid

def set_position_macgyver(position_tuple, maps):
	maps[position_tuple[0]][position_tuple[1]] = 'M'
	return maps

def set_position_gardien(position_tuple, maps):
	maps[position_tuple[0]][position_tuple[1]] = 'G'
	return maps

def set_position_objet(position_tuple, maps):
	maps[position_tuple[0]][position_tuple[1]] = 'O'
	return maps

def get_position_macgyver(maps):
	for (i, line) in enumerate(maps):
		for (j, character) in enumerate(line):
			if character == 'M':
				return(j,i)


def draw(maps):
	for line in maps:
		for character in line:
			print(character,  end='' )
		print('\n', end='')
