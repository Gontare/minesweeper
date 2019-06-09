import random

from minesweeper.environment.node import Node


class Bomb(Node):
    def __init__(self, x, y, direction, cost, timer):
        super().__init__(x, y)
        self.direction = direction
        self.cost = cost
        self.timer = timer
        self.type = random.randint(1, 4)

    @staticmethod
    def generate_bombs():
        bombs_pos = [(1, 2), (1, 4), (1, 8), (1, 10), (1, 12), (1, 14),
                    (3, 2), (3, 4), (3, 8), (3, 10), (3, 12), (3, 14),
                    (5, 2), (5, 4), (5, 8), (5, 10), (5, 12), (5, 14),
                    (7, 2), (7, 4), (7, 8), (7, 10), (7, 12), (7, 14),
                    (9, 2), (9, 4), (9, 8), (9, 10), (9, 12), (9, 14),
                    (11, 2), (11, 4), (11, 8), (11, 10), (11, 12), (11, 14),
                    (13, 2), (13, 4), (13, 8), (13, 10), (13, 12), (13, 14)
                    ]
        random_int = random.randint(0, 41)

        return bombs_pos[random_int]
