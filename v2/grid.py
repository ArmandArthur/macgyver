
import os
import sys

def loading(data_file):
	
	directory = os.path.dirname(__file__)
	path_to_file = os.path.join(directory, 'data', data_file)
	
	grid = []

	with open(path_to_file) as file:
		for line in file:
			grid.append(line)

	return grid

def transform(grid):

	grid_transform = {}

	for i, line in enumerate(grid):
		grid_transform[i] = {}
		for j, case in enumerate(line):
			grid_transform[i][j] = case

	return grid_transform

def draw(grid_transform):
	for i in list(grid_transform):
		print('',  end = '\r' )
		for j in list(grid_transform[i]):
			print(grid_transform[i][j],  end = '')


def free(grid_transform):

	grid_transform_copy = list(grid_transform)
	for i in grid_transform_copy:
		for j in grid_transform_copy[i]:
			if grid_transform_copy[i][j] == 'X' or grid_transform_copy[i][j] == '\n' or grid_transform_copy[i][j] == 'C':
				grid_transform_copy[i].pop(j)

	return grid_transform_copy


def set_position_character(character_tuple, grid_transform):
    grid_transform[character_tuple[0]][character_tuple[1]] = 'C'
    return grid_transform

