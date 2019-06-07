from minesweeper.Astar.SquareGrid import SquareGrid


class GridWithWeights(SquareGrid):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.weights = {}

    def cost(self, to_node):
        return self.weights.get(to_node, 1)
