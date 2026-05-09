from collections import deque

class TerritoryManager:
    def __init__(self, graph, actors):
        self.graph = graph
        self.actors = actors

    def update(self):
        visited = set()

        for node in self.graph.nodes.values():
            if node.owner is not None:
                continue

            if node in visited:
                continue

            region = self._collect_region(node)
            visited.update(region)

            reachable_players = self._get_reachable_players(region)

            if len(reachable_players) == 1:
                owner = next(iter(reachable_players))
                self._claim_region(region, owner)

    def _collect_region(self, start):
        region = set()
        queue = deque([start])

        while queue:
            node = queue.popleft()

            if node in region:
                continue

            if node.owner is not None:
                continue

            region.add(node)

            for neighbor in self.graph.get_neighbors(node, None):
                if neighbor.owner is None:
                    queue.append(neighbor)

        return region

    def _get_reachable_players(self, region):
        reachable = set()

        for node in region:
            x = node.grid_x
            y = node.grid_y

            if y % 2 == 0:
                directions = [(-1, -1), (0, -1), (1, 0), (0, 1), (-1, 1), (-1, 0)]
            else:
                directions = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 0)]

            for dx, dy in directions:
                neighbor = self.graph.get_node(x + dx, y + dy)

                if neighbor and neighbor.owner is not None:
                    reachable.add(neighbor.owner)

        return reachable

    def _claim_region(self, region, player):
        for node in region:
            node.owner = player
            node.color = player.color
            player.points += node.move_cost
            node.move_cost = 0