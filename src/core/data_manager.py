import json
import os
from core.graph import Graph

class DataManager:
    def __init__(self, map_dir="maps"):
        self.map_dir = map_dir
        if not os.path.exists(self.map_dir):
            os.makedirs(self.map_dir)

    def save_map(self, filename, graph):
        map_data = {
            "cols": graph.cols,
            "rows": graph.rows,
            "tile_width": graph.tile_width,
            "tile_height": graph.tile_height,
            "nodes": []
        }
        for coords, node in graph.nodes.items():
            node_info = {
                "x": node.grid_x,
                "y": node.grid_y,
                "weight": node.weight,
                "owner_name": node.owner.name if node.owner else None
            }
            map_data["nodes"].append(node_info)
        filepath = os.path.join(self.map_dir, filename)
        with open(filepath, 'w') as f:
            json.dump(map_data, f, indent=4)

    def load_map(self, filename, actors=None):
        filepath = os.path.join(self.map_dir, filename)
        if not os.path.exists(filepath):
            return None
        with open(filepath, 'r') as f:
            data = json.load(f)
        new_graph = Graph(data["cols"], data["rows"], data["tile_width"], data["tile_height"])
        actor_lookup = {a.name: a for a in actors} if actors else {}
        for node_data in data["nodes"]:
            x, y = node_data["x"], node_data["y"]
            weight = node_data["weight"]
            owner_name = node_data.get("owner_name")
            node = new_graph.get_node(x, y)
            if node:
                node.set_weight(weight)
                if owner_name in actor_lookup:
                    node.capture(actor_lookup[owner_name])
        return new_graph

    def list_maps(self):
        return [f for f in os.listdir(self.map_dir) if f.endswith('.json')]