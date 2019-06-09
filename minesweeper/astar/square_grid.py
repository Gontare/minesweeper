class SquareGrid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.walls = []

    def in_bounds(self, tile_id):
        (x, y) = tile_id
        return 0 <= x < self.width and 0 <= y < self.height

    def passable(self, tile_id):
        return tile_id not in self.walls

    def neighbors(self, tile_id):
        (x, y) = tile_id
        results = [(x + 1, y), (x, y - 1), (x - 1, y), (x, y + 1)]
        if (x + y) % 2 == 0:
            results.reverse()  # aesthetics
        results = filter(self.in_bounds, results)
        results = filter(self.passable, results)
        return results
