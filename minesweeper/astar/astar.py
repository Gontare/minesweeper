from minesweeper.astar.grid_with_weights import GridWithWeights
from minesweeper.astar.priority_queue import PriorityQueue


class Astar:
    def __init__(self):
        self.start = (0, 0)
        self.diagram = GridWithWeights(15, 15)
        self.DIAGRAM_WALLS = [(3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (3, 10), (3, 11),
                              (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (11, 8), (11, 9), (11, 10), (11, 11)]

    @staticmethod
    def heuristic(a, b):
        (x1, y1) = a
        (x2, y2) = b
        return abs(x1 - x2) + abs(y1 - y2)

    @staticmethod
    def reconstruct_path(came_from, start, goal):
        current = goal
        path = []
        while current != start:
            path.append(current)
            current = came_from[current]
        path.append(start)  # optional
        path.reverse()  # optional
        return path

    def a_star_search(self, graph, start, goal):
        frontier = PriorityQueue()
        frontier.put(start, 0)
        came_from = {}
        cost_so_far = {}
        came_from[start] = None
        cost_so_far[start] = 0

        while not frontier.empty():
            current = frontier.get()

            if current == goal:
                break

            for next_neighbour in graph.neighbors(current):
                new_cost = cost_so_far[current] + graph.cost(current, next_neighbour)
                if next_neighbour not in cost_so_far or new_cost < cost_so_far[next_neighbour]:
                    cost_so_far[next_neighbour] = new_cost
                    priority = new_cost + self.heuristic(goal, next_neighbour)
                    frontier.put(next_neighbour, priority)
                    came_from[next_neighbour] = current

        return came_from, cost_so_far

    # utility functions for dealing with square grids
    def from_id_width(id, width):
        return id % width, id // width

    @staticmethod
    def draw_tile(graph, tile_id, style, width):
        r = "."
        if 'number' in style and tile_id in style['number']: r = "%d" % style['number'][tile_id]
        if 'point_to' in style and style['point_to'].get(tile_id, None) is not None:
            (x1, y1) = tile_id
            (x2, y2) = style['point_to'][tile_id]
            if x2 == x1 + 1:
                r = ">"
            if x2 == x1 - 1:
                r = "<"
            if y2 == y1 + 1:
                r = "v"
            if y2 == y1 - 1:
                r = "^"
        if 'start' in style and tile_id == style['start']:
            r = "A"
        if 'goal' in style and tile_id == style['goal']:
            r = "Z"
        if 'path' in style and tile_id in style['path']:
            r = "@"
        if tile_id in graph.walls:
            r = "#" * width
        return r

    def draw_grid(self, graph, width=2, **style):
        for y in range(graph.height):
            for x in range(graph.width):
                print("%%-%ds" % width % self.draw_tile(graph, (x, y), style, width), end="")
            print()

    def sprite_move(self, start, goal):
        diagram = GridWithWeights(15, 15)
        diagram.walls = self.DIAGRAM_WALLS
        came_from, cost_so_far = self.a_star_search(diagram, start, goal)
        self.draw_grid(diagram, width=3, point_to=came_from, start=start, goal=goal)
        self.draw_grid(diagram, width=3, number=cost_so_far, start=start, goal=goal)
        return self.reconstruct_path(came_from, start=start, goal=goal)
