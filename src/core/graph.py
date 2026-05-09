from .node import Node

class Graph:
    def __init__(self, cols, rows, tile_width=64, tile_height=64):
        self.cols = cols
        self.rows = rows
        self.tile_width = tile_width
        self.tile_height = tile_height
        self.nodes = {}

        self.gen_graph()

    def gen_graph(self):
        for y in range(self.rows):
            for x in range(self.cols):
                self.nodes[(x, y)] = Node(
                    x,
                    y,
                    self.tile_width,
                    self.tile_height
                )

    def get_node(self, x, y):
        return self.nodes.get((x, y))

    def get_neighbors(self, node, current_actor):
        x = node.grid_x
        y = node.grid_y

        neighbors = []

        if y % 2 == 0:
            directions = [
                (-1, -1),
                (0, -1),
                (1, 0),
                (0, 1),
                (-1, 1),
                (-1, 0)
            ]
        else:
            directions = [
                (0, -1),
                (1, -1),
                (1, 0),
                (1, 1),
                (0, 1),
                (-1, 0)
            ]

        for dx, dy in directions:
            target = self.get_node(x + dx, y + dy)

            if target:
                if current_actor is None:
                    neighbors.append(target)
                elif target.owner is None or target.owner == current_actor:
                    neighbors.append(target)

        return neighbors