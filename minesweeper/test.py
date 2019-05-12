from minesweeper.implementation import *

start, goal = (0, 0), (7, 8)

came_from, cost_so_far = a_star_search(diagram4, start, goal)
draw_grid(diagram4, width=3, point_to=came_from, start=start, goal=goal)
# print()
draw_grid(diagram4, width=3, number=cost_so_far, start=start, goal=goal)
# print()
draw_grid(diagram4, width=3, path=reconstruct_path(came_from, start=start, goal=goal))


def goal(tilemap, bombcounter):
    x = 0
    y = 0
    z = 1
    for x in range(15):
        if z == 0:
            break
        for y in range(15):
            if tilemap[x][y] == 1:
                # print(x , " " , y)
                tilemap[x][y] = 3
                bombcounter -= 1
                z = 0
            if z == 0:
                break
    return x, y


def spritemove(start, goal):
        came_from, cost_so_far = a_star_search(diagram4, start, goal)
        # draw_grid(diagram4, width=3, path=reconstruct_path(came_from, start=start, goal=goal))
        return reconstruct_path(came_from, start=start, goal=goal)
