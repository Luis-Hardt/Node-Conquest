import json
import os
from .graph import Graph
from .node import Node

class DataManager:
    def __init__(self, map_dir="maps"):
        self.map_dir = map_dir
        if not os.path.exists(self.map_dir):
            os.makedirs(self.map_dir)

    def save_map(self, filename, graph):
        map_data = {
            "width": graph.width,
            "height": graph.height,
            "tile_size": graph.tile_size,
            "nodes": []
        }
        
        for coords, node in graph.nodes.items():
            node_info = {
                "x": node.grid_x,
                "y": node.grid_y,
                "terrain": node.terrain_type,
                "owner": node.owner
            }
            map_data["nodes"].append(node_info)

        filepath = os.path.join(self.map_dir, filename)
        with open(filepath, 'w') as f:
            json.dump(map_data, f, indent=4)

    def load_map(self, filename):
        filepath = os.path.join(self.map_dir, filename)
        if not os.path.exists(filepath):
            return None

        with open(filepath, 'r') as f:
            data = json.load(f)

        new_graph = Graph(data["width"], data["height"], data["tile_size"])
        
        for node_data in data["nodes"]:
            x, y = node_data["x"], node_data["y"]
            terrain = node_data["terrain"]
            owner = node_data["owner"]
            
            new_node = Node(x, y, data["tile_size"], terrain_type=terrain)
            new_node.owner = owner
            new_graph.nodes[(x, y)] = new_node
            
        return new_graph

    def list_maps(self):
        return [f for f in os.listdir(self.map_dir) if f.endswith('.json')]