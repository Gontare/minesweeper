class Node:
    def __init__(self, direction, cost):
        self.x = 0
        self.y = 0
        self.direction = direction
        self.cost = cost

    @staticmethod
    def generate_nodes():
        nodes = [Node(0, 0) for i in range(225)]
        for node in nodes:
            listONodes = [node]
            print(listONodes)

    def get_pos(self):
        return self.x, self.y

