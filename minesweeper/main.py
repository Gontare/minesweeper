import pygame as pg

from minesweeper.agent import Agent
from minesweeper.grid import Grid

# initializing PyGame module
pg.init()
print('This is our intelligent sprite running through a minefield!')
pg.display.set_caption('Minesweeper')

# agent object
agent = Agent()

# grid object
grid = Grid()


def main():
    grid.set_tilemap()
    grid.generate_tilemap()

    # game loop
    while True:
        # initiating clock
        dt = pg.time.get_ticks()
        TIME = (dt / 1000) % 60

        # tiles
        TILES = 0

        # mines
        MINES = 0

        # getting mines demined
        grid.legend(TIME, TILES, MINES)

        # displaying the grid
        grid.display_tilemap()

        # agent movement event
        agent.agent_move(grid.tilemap, grid.MAPWIDTH, grid.MAPHEIGHT)

        # agent display
        agent.show_agent(grid.TILESIZE, grid.SURFACE)
        pg.display.update()


if __name__ == "__main__":
    main()
