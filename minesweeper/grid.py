import random

import pygame as pg


class Grid:

    def __init__(self):
        # display dimensions
        self.TILESIZE = 40
        self.MAPHEIGHT = 15
        self.MAPWIDTH = 15

        # colors
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)

        # floors accessible
        self.GROUND = 0
        self.LANDMINE = 1
        # not accessible
        self.OBSTACLE = 2
        self.DEMINED = 3
        self.PATH = 4
        self.START = 5

        self.floor = [self.GROUND, self.LANDMINE, self.OBSTACLE, self.DEMINED, self.PATH, self.START]

        # dictionary linking textures with floors
        self.textures = {
            self.GROUND: pg.image.load('resources/ground.png'),
            self.OBSTACLE: pg.image.load('resources/obstacle.png'),
            self.LANDMINE: pg.image.load('resources/landmine.png'),
            self.DEMINED: pg.image.load('resources/demined.png'),
            self.PATH: pg.image.load('resources/path.png'),
            self.START: pg.image.load('resources/start.png')
        }

        # a list representing our tilemap
        self.tilemap = []
        self.bombcounter = 0

        # creating a new drawing surface
        self.SURFACE = pg.display.set_mode((self.TILESIZE * self.MAPWIDTH, self.TILESIZE * self.MAPHEIGHT + 50))

    def wall_up(self):
        for x in range(4, 5):
            for y in range(3, 12):
                self.tilemap[x][y] = self.OBSTACLE

        for x in range(10, 11):
            for y in range(3, 12):
                self.tilemap[x][y] = self.OBSTACLE

    def generate_tilemap(self):
        # randomly generated flooring
        for rw in range(self.MAPHEIGHT):
            for cl in range(self.MAPWIDTH):
                num = random.randint(0, 14)
                if num < 13:
                    tile = self.GROUND
                # elif 10 <= num < 13:
                    # tile = self.OBSTACLE
                else:
                    tile = self.LANDMINE
                    self.bombcounter += 1
                self.tilemap[rw][cl] = tile
                self.tilemap[0][0] = self.START
                self.wall_up()

    def set_tilemap(self):
        self.tilemap = [[self.GROUND for w in range(self.MAPWIDTH)] for h in range(self.MAPHEIGHT)]
        return self.tilemap

    def display_tilemap(self):
        for row in range(self.MAPHEIGHT):
            for column in range(self.MAPWIDTH):
                # pg.draw.rect(SURFACE, colors[tilemap[row][column]],
                # (column*TILESIZE, row*TILESIZE, TILESIZE, TILESIZE))
                self.SURFACE.blit(self.textures[self.tilemap[row][column]],
                                  (row * self.TILESIZE, column * self.TILESIZE))

    def how_many_demined(self):
        counter = 0
        for row in range(self.MAPHEIGHT):
            for column in range(self.MAPWIDTH):
                if self.tilemap[row][column] == self.DEMINED:
                    counter += 1
        return counter

    # REFACTOR
    def show_screen(self, MINES):
        # mouse is not visible
        pg.mouse.set_visible(False)

        # font for show_screen
        FONT = pg.font.Font(None, 40)

        # show_screen bar
        placePosition = 50

        if self.bombcounter != 0:
            # clock show_screen
            # clock_image = pg.image.load('resources/clock.png')
            # self.SURFACE.blit(clock_image, (placePosition, self.MAPHEIGHT * self.TILESIZE + 5))
            # placePosition += 50
            # textObj1 = FONT.render(str(TIME), True, self.WHITE, self.BLACK)
            # self.SURFACE.blit(textObj1, (placePosition, self.MAPHEIGHT * self.TILESIZE + 13))
            # placePosition += 120

            # mines uncovered show_screen
            mines = pg.image.load('resources/mines.png')
            self.SURFACE.blit(mines, (placePosition, self.MAPHEIGHT * self.TILESIZE + 5))
            placePosition += 50
            textObj3 = FONT.render(str(MINES), True, self.WHITE, self.BLACK)
            self.SURFACE.blit(textObj3, (placePosition, self.MAPHEIGHT * self.TILESIZE + 13))
