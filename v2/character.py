
import random


def create(grid_transform):
    position_x_random = random.choice(list(grid_transform.keys()))
    position_y_random = random.choice(list(grid_transform[position_x_random]))
    return (position_x_random, position_y_random)
