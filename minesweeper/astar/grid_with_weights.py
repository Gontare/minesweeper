from minesweeper.astar.square_grid import SquareGrid


class GridWithWeights(SquareGrid):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.weights = {}

    def cost(self, fromNode, toNode):
        return self.weights.get(toNode, 1)
