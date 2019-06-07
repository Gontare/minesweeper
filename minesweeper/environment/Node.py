import pygame as pg
import numpy as np


class Node:
    def __init__(self, x, y, direction, cost):
        self.x = x
        self.y = y
        self.position = (x, y)
        self.direction = direction
        self.cost = cost
        self.grid = np.array([(x, y, direction)], [])
