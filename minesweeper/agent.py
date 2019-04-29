import random
import sys

import pygame as pg


class Agent:
    def __init__(self):
        pass

    playerPos = [0, 0]
    AGENT = pg.image.load("resources/agent.png")

    def move_right(self):
        x += 1

    def move_left(self):
        x -= 1

    def move_up(self):
        y += 1

    def move_down(self):
        y -= 1

    def show_agent(self, tilesize, SURFACE):
        SURFACE.blit(self.AGENT, (self.playerPos[0] * tilesize, self.playerPos[1] * tilesize))

    def player_pos(self):
        print(x + " " + y)

    def demine(self, tilemap):
        if tilemap[self.playerPos[0]][self.playerPos[1]] == 1:
            tilemap[self.playerPos[0]][self.playerPos[1]] = 3

    def agent_move(self, tilemap, MAPWIDTH, MAPHEIGHT):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
        while True:
            way = random.randint(1, 4)
            # print(way)
            # print("tilemap:" + str(tilemap[self.playerPos[0]][self.playerPos[1]]) + " " + str(self.playerPos[0])
            # + " " + str(self.playerPos[1]))

            if way == 1 and self.playerPos[0]< MAPWIDTH - 1:
                if self.playerPos[0] < 15:
                    if tilemap[self.playerPos[0] + 1][self.playerPos[1]] != 2:
                        self.playerPos[0] += 1
                        self.demine(tilemap)
                        # print(self.playerPos[0], self.playerPos[1])
                        break
            if way == 2 and self.playerPos[0] > 0:
                if self.playerPos[0] < 15:
                    if tilemap[self.playerPos[0] - 1][self.playerPos[1]] != 2:
                        self.playerPos[0] -= 1
                        self.demine(tilemap)
                        # print(self.playerPos[0], self.playerPos[1])
                        break
            if way == 3 and self.playerPos[1] < MAPHEIGHT - 1:
                if self.playerPos[0] < 15:
                    if tilemap[self.playerPos[0]][self.playerPos[1] + 1] != 2:
                        self.playerPos[1] += 1
                        self.demine(tilemap)
                        # print(self.playerPos[0], self.playerPos[1])
                break
            if way == 4 and self.playerPos[1] > 0:
                if self.playerPos[0] < 15:
                    if tilemap[self.playerPos[0]][self.playerPos[1] - 1] != 2:
                        self.playerPos[1] -= 1
                        self.demine(tilemap)
                        # print(self.playerPos[0], self.playerPos[1])
                        break

'''
            if way == 1 and playerPos[0] < MAPWIDTH - 1 and 
                playerPos[0] += 1
                print(playerPos[0], playerPos[1])
                break
            if way == 2 and playerPos[0] > 0 and tilemap[playerPos[0] - 1][playerPos[1]] != 2:
                playerPos[0] -= 1
                print(playerPos[0], playerPos[1])
                break
            if way == 3 and playerPos[1] < MAPHEIGHT - 1 and tilemap[playerPos[0]][playerPos[1] + 1] != 2:
                playerPos[1] += 1
                print(playerPos[0], playerPos[1])
                break
            if way == 4 and playerPos[1] > 0 and tilemap[playerPos[0]][playerPos[1] - 1] != 2:
                playerPos[1] -= 1
                print(playerPos[0], playerPos[1])
                break
'''
