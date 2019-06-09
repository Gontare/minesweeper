import numpy as np
import pygame as pg

from minesweeper.environment.bomb import Bomb


class Grid:
    def __init__(self):
        # display dimensions
        self.TILE_SIZE = 40
        self.MAPHEIGHT = 15
        self.MAPWIDTH = 15

        # colors
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)

        # floors
        self.GROUND = 0
        self.WALL = 1
        self.DEMINED = 2
        self.START = 3
        self.LANDMINE_N = 4
        self.LANDMINE_E = 5
        self.LANDMINE_S = 6
        self.LANDMINE_W = 7

        # list of types of flooring
        self.floor = [self.GROUND, self.WALL, self.DEMINED, self.START,
                      self.LANDMINE_N, self.LANDMINE_E, self.LANDMINE_S, self.LANDMINE_W]

        # dictionary linking textures with floors
        self.textures = {
            self.GROUND: pg.image.load('resources/ground.png'),
            self.WALL: pg.image.load('resources/obstacle.png'),
            self.DEMINED: pg.image.load('resources/demined.png'),
            self.START: pg.image.load('resources/start.png'),
            self.LANDMINE_N: pg.image.load('resources/landmine_n.png'),
            self.LANDMINE_E: pg.image.load('resources/landmine_e.png'),
            self.LANDMINE_S: pg.image.load('resources/landmine_s.png'),
            self.LANDMINE_W: pg.image.load('resources/landmine_w.png')
        }

        # a list representing our tilemap
        self.tilemap = []
        self.bombCounter = 0

        # creating a new drawing surface
        self.SURFACE = pg.display.set_mode((self.TILE_SIZE * self.MAPWIDTH, self.TILE_SIZE * self.MAPHEIGHT))

        # grid list for wall generation
        self.grid = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # column 1 reversed
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # column 2 reversed
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # column 3 reversed
                             [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],  # column 4 reversed
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # and so on...
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                              ])

    def wall_up(self, x, y):
        self.tilemap[x][y] = self.WALL

    def place_bombs(self):
        for x in range(9):
            bomb_pos = Bomb.generate_bombs()
            bomb = Bomb(bomb_pos[0], bomb_pos[1], 0, 0, 0)
            if bomb.type == 1:
                self.tilemap[bomb_pos[0]][bomb_pos[1]] = self.LANDMINE_N
            elif bomb.type == 2:
                self.tilemap[bomb_pos[0]][bomb_pos[1]] = self.LANDMINE_E
            elif bomb.type == 3:
                self.tilemap[bomb_pos[0]][bomb_pos[1]] = self.LANDMINE_S
            else:
                self.tilemap[bomb_pos[0]][bomb_pos[1]] = self.LANDMINE_W

    def generate_tilemap(self):
        # start and end
        self.tilemap[0][0] = self.START
        self.tilemap[14][14] = self.START

        # call to method which shows bombs
        self.place_bombs()

        for x in range(0, 14):
            for y in range(0, 14):
                if self.grid[x][y] == 1:
                    # call to wall_up method which generates bombs
                    self.wall_up(x, y)

        return self.tilemap

    def count_bombs(self):
        for rw in range(self.MAPHEIGHT):
            for cl in range(self.MAPWIDTH):
                if self.tilemap[rw][cl] == self.LANDMINE_N or self.LANDMINE_E or self.LANDMINE_S or self.LANDMINE_W:
                    self.bombCounter += 1

    def set_tilemap(self):
        self.tilemap = [[self.GROUND for width in range(self.MAPWIDTH)] for height in range(self.MAPHEIGHT)]
        return self.tilemap

    def display_tilemap(self):
        for row in range(self.MAPHEIGHT):
            for column in range(self.MAPWIDTH):
                # pg.draw.rect(SURFACE, colors[tilemap[row][column]],
                # (column*TILE_SIZE, row*TILE_SIZE, TILE_SIZE, TILE_SIZE))
                self.SURFACE.blit(self.textures[self.tilemap[row][column]],
                                  (row * self.TILE_SIZE, column * self.TILE_SIZE))

