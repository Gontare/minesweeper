import pygame as pg

from minesweeper.sprite import Sprite
from minesweeper.grid import Grid

# initializing PyGame module
pg.init()
print('This is our intelligent sprite running through a minefield!')
pg.display.set_caption('Minesweeper')

# agent object
agent = Sprite()

# grid object
grid = Grid()


def main():
    grid.set_tilemap()
    grid.generate_tilemap()
    grid.count_bombs()
    print(grid.tilemap)

    # game loop
    while True and grid.bombcounter != 0:
        # initiating clock
        # dt = pg.time.get_ticks()
        # TIME = (dt / 1000) % 60
        # sec = str(TIME).split('.')
        # TIME = sec[0]

        # displaying the grid
        grid.display_tilemap()

        move = agent.move_sprite(grid.tilemap, grid.bombcounter)
        print(agent.goal)
        move.extend([agent.goal])

        # mines
        MINES = grid.bombcounter

        # shows our screen with legend
        grid.show_screen(MINES)

        for x in range(len(move)):
            sprite_movement = move[x]
            # print(sprite_movement)
            # print(agent.spritePos)
            agent.spritePos[0] = sprite_movement[0] - 1
            agent.spritePos[1] = sprite_movement[1] - 1
            agent.show_sprite(grid.TILESIZE, grid.SURFACE)

            pg.time.wait(30)
            pg.display.update()
            grid.SURFACE.blit(grid.textures[grid.tilemap[agent.spritePos[0]][agent.spritePos[1]]], (agent.spritePos[0] * grid.TILESIZE, agent.spritePos[1] * grid.TILESIZE))

        pg.time.wait(1000)

        # display update
        pg.display.update()


if __name__ == "__main__":
    main()
