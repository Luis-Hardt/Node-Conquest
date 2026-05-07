import heapq

class AStar:
    def __init__(self, graph):
        self.graph = graph

    def heuristic(self, a, b):
        ax, ay = a.grid_x, a.grid_y
        bx, by = b.grid_x, b.grid_y
        
        az = -(ax + ay) if ay % 2 == 0 else -(ax + ay + 1)
        bz = -(bx + by) if by % 2 == 0 else -(bx + by + 1)
        
        return max(abs(ax - bx), abs(ay - by), abs(az - bz))

    def get_path(self, start_node, goal_node):
        frontier = []
        heapq.heappush(frontier, (0, start_node))
        
        came_from = {start_node: None}
        cost_so_far = {start_node: 0}

        while frontier:
            current = heapq.heappop(frontier)[1]

            if current == goal_node:
                break

            for next_node in self.graph.get_neighbors(current):
                new_cost = cost_so_far[current] + next_node.move_cost
                
                if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                    cost_so_far[next_node] = new_cost
                    priority = new_cost + self.heuristic(goal_node, next_node)
                    heapq.heappush(frontier, (priority, next_node))
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