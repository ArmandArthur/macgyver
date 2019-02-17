"""
    Import random
"""
import random

class Object:
    """
        Set the position of object random
    """
    def __init__(self, grid):
        position_x = random.randint(0, 14)
        position_y = random.randint(0, 14)
        while grid[position_x][position_y] != ' ':
            position_x = random.randint(0, 14)
            position_y = random.randint(0, 14)
        self.position_x = position_x
        self.position_y = position_y
