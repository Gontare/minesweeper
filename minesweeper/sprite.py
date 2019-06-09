import sys
import pygame as pg


class Sprite:
    def __init__(self):
        super().__init__()
        self.spritePos = [0, 0]
        self.SPRITE = pg.image.load('resources/agent.png')
        self.previousGoal = (0, 0)
        self.goal = []
        self.count = 0

    @staticmethod
    def sprite_goal(tilemap, bomb_counter):
        x = 0
        y = 0
        z = 1

        for x in range(15):
            if z == 0:
                break
            for y in range(15):
                if tilemap[x][y] == 4 or tilemap[x][y] == 5 or tilemap[x][y] == 6 or tilemap[x][y] == 7:
                    # print(x , " " , y)
                    tilemap[x][y] = 2
                    bomb_counter -= 1
                    z = 0
                if z == 0:
                    break

        return x, y

    def show_sprite(self, tile_size, surface):
        surface.blit(self.SPRITE, (self.spritePos[0] * tile_size, self.spritePos[1] * tile_size))

    def move_sprite(self, tilemap, bomb_counter):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

#       SPRITE MOVEMENT V3
#       astar = Astar()
#       if self.count == 0:
#           self.count = 1
#           self.goal = self.sprite_goal(tilemap, bomb_counter)
#       else:
#           self.previousGoal = self.goal
#           self.goal = self.sprite_goal(tilemap, bomb_counter)
#       return Astar.sprite_move(astar, self.previousGoal, self.goal)

#        SPRITE MOVEMENT V2
#        while True:
#            sprite movement v2
#            way = random.randint(1, 4)
#            print(way)
#            print("tilemap:" + str(tilemap[self.spritePos[0]][self.spritePos[1]]) + " " + str(self.spritePos[0])
#            + " " + str(self.spritePos[1]))

#            if way == 1 and self.spritePos[0]< MAPWIDTH - 1:
#               if self.spritePos[0] < 15:
#                   if tilemap[self.spritePos[0] + 1][self.spritePos[1]] != 2:
#                       self.spritePos[0] += 1
#                       self.demine(tilemap)
#                       print(self.spritePos[0], self.spritePos[1])
#                       break
#            if way == 2 and self.spritePos[0] > 0:
#               if self.spritePos[0] < 15:
#                   if tilemap[self.spritePos[0] - 1][self.spritePos[1]] != 2:
#                       self.spritePos[0] -= 1
#                       self.demine(tilemap)
#                       print(self.spritePos[0], self.spritePos[1])
#                       break
#            if way == 3 and self.spritePos[1] < MAPHEIGHT - 1:
#               if self.spritePos[0] < 15:
#                   if tilemap[self.spritePos[0]][self.spritePos[1] + 1] != 2:
#                       self.spritePos[1] += 1
#                       self.demine(tilemap)
#                       print(self.spritePos[0], self.spritePos[1])
#                       break
#            if way == 4 and self.spritePos[1] > 0:
#               if self.spritePos[0] < 15:
#                   if tilemap[self.spritePos[0]][self.spritePos[1] - 1] != 2:
#                       self.spritePos[1] -= 1
#                       self.demine(tilemap)
#                       print(self.spritePos[0], self.spritePos[1])
#                       break

#        SPRITE MOVEMENT V1
#        if way == 1 and spritePos[0] < MAPWIDTH - 1 and
#             spritePos[0] += 1
#             print(spritePos[0], spritePos[1])
#             break
#        if way == 2 and spritePos[0] > 0 and tilemap[spritePos[0] - 1][spritePos[1]] != 2:
#             spritePos[0] -= 1
#             print(spritePos[0], spritePos[1])
#             break
#        if way == 3 and spritePos[1] < MAPHEIGHT - 1 and tilemap[spritePos[0]][spritePos[1] + 1] != 2:
#             spritePos[1] += 1
#             print(spritePos[0], spritePos[1])
#             break
#        if way == 4 and spritePos[1] > 0 and tilemap[spritePos[0]][spritePos[1] - 1] != 2:
#             spritePos[1] -= 1
#             print(spritePos[0], spritePos[1])
#             break
