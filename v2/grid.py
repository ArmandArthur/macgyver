
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

	for i, line in enumerate(grid_transform):
		print('',  end = '\r' )
		for j, case in enumerate(grid_transform[i]):
		    print(grid_transform[i][j],  end = '')



