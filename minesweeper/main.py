import pygame as pg

from minesweeper.sprite import Sprite
from minesweeper.environment.grid import Grid

# initializing PyGame module
pg.init()
print('This is our intelligent sprite running through a minefield!')
pg.display.set_caption('Minesweeper')
pg.mouse.set_visible(False)

# grid object
grid = Grid()

# agent object
agent = Sprite()


def main():
    grid.set_tilemap()
    grid.generate_tilemap()
    grid.count_bombs()

    # game loop
    while True and grid.bomb_counter != 0:
        # initiating clock
        # dt = pg.time.get_ticks()
        # TIME = (dt / 1000) % 60
        # sec = str(TIME).split('.')
        # TIME = sec[0]

        # displaying the grid
        grid.display_tilemap()

        move = agent.move_sprite(grid.tilemap, grid.bomb_counter)
        move.extend([agent.goal])

        for x in range(len(move)):
            print(agent.spritePos)
            sprite_movement = move[x]
            agent.spritePos[0] = sprite_movement[0] - 1
            agent.spritePos[1] = sprite_movement[1] - 1
            agent.show_sprite(grid.TILE_SIZE, grid.SURFACE)
            pg.time.wait(30)
            pg.display.update()
            grid.SURFACE.blit(grid.textures[grid.tilemap[agent.spritePos[0]][agent.spritePos[1]]], (agent.spritePos[0]
                * grid.TILE_SIZE, agent.spritePos[1] * grid.TILE_SIZE))

        pg.time.wait(1000)

        # display update
        pg.display.update()


if __name__ == "__main__":
    main()
