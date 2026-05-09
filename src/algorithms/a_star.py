import heapq
import itertools

class AStar:
    def __init__(self, graph):
        self.graph = graph

    def _to_cube(self, node):
        q = node.grid_x - (node.grid_y - (node.grid_y % 2)) // 2
        r = node.grid_y
        s = -q - r
        return q, r, s

    def heuristic(self, a, b):
        aq, ar, as_ = self._to_cube(a)
        bq, br, bs = self._to_cube(b)
        return max(abs(aq - bq), abs(ar - br), abs(as_ - bs))

    def get_path(self, start_node, goal_node, actor):
        frontier = []
        counter = itertools.count()
        heapq.heappush(frontier, (0, next(counter), start_node))
        came_from = {start_node: None}
        cost_so_far = {start_node: 0}
        
        while frontier:
            current = heapq.heappop(frontier)[2]
            if current == goal_node:
                break
            for next_node in self.graph.get_neighbors(current, actor):
                new_cost = cost_so_far[current] + next_node.move_cost
                if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                    cost_so_far[next_node] = new_cost
                    priority = new_cost + self.heuristic(goal_node, next_node)
                    heapq.heappush(frontier, (priority, next(counter), next_node))
                    came_from[next_node] = current
        return self._reconstruct_path(came_from, start_node, goal_node)

    def _reconstruct_path(self, came_from, start, goal):
        if goal not in came_from:
            return []
        current = goal
        path = []
        while current != start:
            path.append(current)
            current = came_from[current]
        path.reverse()
        return path