from .node import Node

class Graph:
    def __init__(self, width, height, tile_size):
        self.width     = width
        self.height    = height
        self.tile_size = tile_size
        self.nodes     = {}
        
        self.gen_graph()

    def gen_graph(self):
        for y in range(self.height):
            for x in range(self.width):
                self.nodes[(x, y)] = Node(x, y, self.tile_size)

    def get_node(self, x, y):
        return self.nodes.get((x, y))

    def get_neighbors(self, node):
        """Returns a list of valid neighboring Node objects."""
        x, y = node.grid_x, node.grid_y
        neighbors = []

        if y % 2 == 0:
            directions = [(1, 0), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1)]
        else:
            directions = [(1, 0), (1, 1), (0, 1), (-1, 0), (0, -1), (1, -1)]

        for dx, dy in directions:
            target = self.get_node(x + dx, y + dy)
            if target:
                neighbors.append(target)
        
        return neighbors

    def draw(self, surface):
        """Renders all nodes in the graph."""
        for node in self.nodes.values():
            node.draw(surface)