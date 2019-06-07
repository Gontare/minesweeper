from minesweeper.astar.grid_with_weights import GridWithWeights
from minesweeper.astar.priority_queue import PriorityQueue


class Astar:
    def __init__(self):
        self.start = (0, 0)
        self.diagram = GridWithWeights(15, 15)
        self.DIAGRAM_WALLS = [(4, 4), (4, 5), (4, 6), (4, 7), (4, 8), (4, 9), (4, 10), (4, 11), (4, 12),
                              (12, 4), (12, 5), (12, 6), (12, 7), (12, 8), (12, 9), (12, 10), (12, 11), (12, 12)]

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

            for next in graph.neighbors(current):
                new_cost = cost_so_far[current] + graph.cost(current, next)
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    priority = new_cost + self.heuristic(goal, next)
                    frontier.put(next, priority)
                    came_from[next] = current

        return came_from, cost_so_far

    def sprite_move(self, start, goal):
        diagram = GridWithWeights(15, 15)
        diagram.walls = self.DIAGRAM_WALLS
        cameFrom, costSoFar = self.a_star_search(diagram, start, goal)
        return self.reconstruct_path(cameFrom, start=start, goal=goal)
