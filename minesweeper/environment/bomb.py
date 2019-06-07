import random

from minesweeper.environment.node import Node


class Bomb(Node):
    def __init__(self, x, y, direction, cost, timer):
        super().__init__(x, y, direction, cost)
        self.timer = timer

    @staticmethod
    def generate_bombs():
        bombsPos = [(2, 2), (2, 4), (2, 8), (2, 10), (2, 12), (2, 14),
                    (4, 2), (4, 4), (4, 8), (4, 10), (4, 12), (4, 14),
                    (6, 2), (6, 4), (6, 8), (6, 10), (6, 12), (6, 14),
                    (8, 2), (8, 4), (8, 8), (8, 10), (8, 12), (8, 14),
                    (10, 2), (10, 4), (10, 8), (10, 10), (10, 12), (10, 14),
                    (12, 2), (12, 4), (12, 8), (12, 10), (12, 12), (12, 14),
                    (14, 2), (14, 4), (14, 8), (14, 10), (14, 12), (14, 14)
                    ]
        randomInt = random.randint(0, 41)

        return bombsPos[randomInt]
