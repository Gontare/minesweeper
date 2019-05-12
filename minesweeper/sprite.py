import sys

import pygame as pg

from minesweeper.test import *


class Sprite:

    def __init__(self):
        self.spritePos = [0, 0]
        self.SPRITE = pg.image.load('resources/agent.png')
        self.length = 0
        self.previous_goal = (0, 0)
        self.goal = None
        self.count1 = 0

    def demine(self, tilemap):
        if tilemap[self.spritePos[0]][self.spritePos[1]] == 1:
            tilemap[self.spritePos[0]][self.spritePos[1]] = 3

    def show_sprite(self, tilesize, SURFACE):
        SURFACE.blit(self.SPRITE, (self.spritePos[0] * tilesize, self.spritePos[1] * tilesize))

    def move_sprite(self, tilemap, bombcounter):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

        # SPRITE MOVEMENT V3
        if self.count1 == 0:
            self.count1 = 1
            self.goal = goal(tilemap, bombcounter)
        else:
            self.previous_goal = self.goal
            self.goal = goal(tilemap, bombcounter)
        return spritemove(self.previous_goal, self.goal)

        # SPRITE MOVEMENT V2
        # while True:
            # sprite movement v2
            # way = random.randint(1, 4)
            # print(way)
            # print("tilemap:" + str(tilemap[self.spritePos[0]][self.spritePos[1]]) + " " + str(self.spritePos[0])
            # + " " + str(self.spritePos[1]))

            # if way == 1 and self.spritePos[0]< MAPWIDTH - 1:
                # if self.spritePos[0] < 15:
                    # if tilemap[self.spritePos[0] + 1][self.spritePos[1]] != 2:
                        # self.spritePos[0] += 1
                        # self.demine(tilemap)
                        # print(self.spritePos[0], self.spritePos[1])
                        # break
            # if way == 2 and self.spritePos[0] > 0:
                # if self.spritePos[0] < 15:
                    # if tilemap[self.spritePos[0] - 1][self.spritePos[1]] != 2:
                        # self.spritePos[0] -= 1
                        # self.demine(tilemap)
                        # print(self.spritePos[0], self.spritePos[1])
                        # break
            # if way == 3 and self.spritePos[1] < MAPHEIGHT - 1:
                # if self.spritePos[0] < 15:
                    # if tilemap[self.spritePos[0]][self.spritePos[1] + 1] != 2:
                        # self.spritePos[1] += 1
                        # self.demine(tilemap)
                        # print(self.spritePos[0], self.spritePos[1])
                # break
            # if way == 4 and self.spritePos[1] > 0:
                # if self.spritePos[0] < 15:
                    # if tilemap[self.spritePos[0]][self.spritePos[1] - 1] != 2:
                        # self.spritePos[1] -= 1
                        # self.demine(tilemap)
                        # print(self.spritePos[0], self.spritePos[1])
                        # break

        # SPRITE MOVEMENT V1
        # if way == 1 and spritePos[0] < MAPWIDTH - 1 and
            # spritePos[0] += 1
            # print(spritePos[0], spritePos[1])
            # break
        # if way == 2 and spritePos[0] > 0 and tilemap[spritePos[0] - 1][spritePos[1]] != 2:
            # spritePos[0] -= 1
            # print(spritePos[0], spritePos[1])
            # break
        # if way == 3 and spritePos[1] < MAPHEIGHT - 1 and tilemap[spritePos[0]][spritePos[1] + 1] != 2:
            # spritePos[1] += 1
            # print(spritePos[0], spritePos[1])
            # break
        # if way == 4 and spritePos[1] > 0 and tilemap[spritePos[0]][spritePos[1] - 1] != 2:
            # spritePos[1] -= 1
            # print(spritePos[0], spritePos[1])
            # break
