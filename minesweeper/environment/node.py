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
            list_o_nodes = [node]
            print(list_o_nodes)

    def get_pos(self):
        return self.x, self.y

