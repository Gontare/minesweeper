import random

import pygame as pg


class Grid:
    # display dimensions
    TILESIZE = 40
    MAPHEIGHT = 15
    MAPWIDTH = 15

    SURFACE = None

    # colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    # floors accessible
    GROUND = 0
    LANDMINE = 1
    # not accessible
    OBSTACLE = 2
    DEMINED = 3
    PATH = 4

    floor = [GROUND, LANDMINE, OBSTACLE, DEMINED, PATH]

    # dictionary linking textures with floors
    textures = {
        GROUND: pg.image.load('resources/ground.png'),
        OBSTACLE: pg.image.load('resources/obstacle.png'),
        LANDMINE: pg.image.load('resources/landmine.png'),
        DEMINED: pg.image.load('resources/demined.png'),
        PATH: pg.image.load('resources/path.png')
    }

    # a list representing our tilemap
    tilemap = []

    def __init__(self):
        pass

    def generate_tilemap(self):
        # randomly generated flooring
        for rw in range(self.MAPHEIGHT):
            for cl in range(self.MAPWIDTH):
                num = random.randint(0, 15)
                if num < 10:
                    tile = self.GROUND
                elif 10 <= num < 13:
                    tile = self.OBSTACLE
                else:
                    tile = self.LANDMINE
                self.tilemap[rw][cl] = tile
                self.tilemap[0][0] = self.GROUND

    def set_tilemap(self):
        self.tilemap = [[self.GROUND for w in range(self.MAPWIDTH)] for h in range(self.MAPHEIGHT)]
        return self.tilemap

    def get_MAPHEIGHT(self):
        return self.MAPHEIGHT

    def get_MAPWIDTH(self):
        return self.MAPHEIGHT

    def display_tilemap(self):
        for row in range(self.MAPHEIGHT):
            for column in range(self.MAPWIDTH):
                # pg.draw.rect(SURFACE, colors[tilemap[row][column]],
                # (column*TILESIZE, row*TILESIZE, TILESIZE, TILESIZE))
                self.SURFACE.blit(self.textures[self.tilemap[row][column]],
                                  (row * self.TILESIZE, column * self.TILESIZE))

    def legend(self, TIME, TILES, MINES):
        # creating a new drawing surface
        self.SURFACE = pg.display.set_mode((self.TILESIZE * self.MAPWIDTH, self.TILESIZE * self.MAPHEIGHT + 50))

        # mouse is not visible
        pg.mouse.set_visible(False)

        # font for legend
        FONT = pg.font.Font(None, 40)

        # legend bar
        placePosition = 100

        # clock legend
        clock_image = pg.image.load('resources/clock.png')
        self.SURFACE.blit(clock_image, (placePosition, self.MAPHEIGHT * self.TILESIZE + 5))
        placePosition += 60
        textObj1 = FONT.render(str(TIME), True, self.WHITE, self.BLACK)
        self.SURFACE.blit(textObj1, (placePosition, self.MAPHEIGHT * self.TILESIZE + 13))
        placePosition += 100

        # tiles legend
        feet = pg.image.load('resources/feet.png')
        self.SURFACE.blit(feet, (placePosition, self.MAPHEIGHT * self.TILESIZE + 5))
        placePosition += 56
        textObj2 = FONT.render(str(TILES), True, self.WHITE, self.BLACK)
        self.SURFACE.blit(textObj2, (placePosition, self.MAPHEIGHT * self.TILESIZE + 13))
        placePosition += 100

        # mines uncovered legend
        mines = pg.image.load('resources/mines.png')
        self.SURFACE.blit(mines, (placePosition, self.MAPHEIGHT * self.TILESIZE + 5))
        placePosition += 60
        textObj3 = FONT.render(str(MINES), True, self.WHITE, self.BLACK)
        self.SURFACE.blit(textObj3, (placePosition, self.MAPHEIGHT * self.TILESIZE + 13))
