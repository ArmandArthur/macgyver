
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

def draw(maps):
	for line in maps:
		for character in line:
			print(character,  end='' )
		print('\n', end='')
