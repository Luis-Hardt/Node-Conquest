import math
import pygame
import os

class Node:
    def __init__(self, x, y, size, terrain_type="plain"):
        self.grid_x = x
        self.grid_y = y
        self.size = size
        self.owner = None
        self.terrain_type = terrain_type
        self.sprite = self._set_sprite(terrain_type)
        self.move_cost = self._set_cost(terrain_type)
        self.color = self._set_color(terrain_type)
        
    def _set_cost(self, terrain_type):
        costs = {"plain": 1, "forest": 2, "hills": 2, "forest_hills": 3, "water": 3}
        return costs.get(terrain_type, 1)

    def _set_color(self, terrain_type):
        colors = {
            "plain"       : (195, 195, 195),
            "forest"      : (195, 255, 195),  
            "hills"       : (235, 225, 195),
            "forest_hills": (255, 255, 255), 
            "water"       : (65, 105, 225)  
        }
        return colors.get(terrain_type, (200, 200, 200))

    def _set_sprite(self, terrain_type):
        terrain_sprites = {
            "plain": "plain.png",
            "forest": "forest.png",
            "hills": "hills.png",
            "forest_hills": "forest_hills.png",
            "water": "water.png"
        }
        filename = terrain_sprites.get(terrain_type)
        
        if filename and os.path.exists(filename):
            try:
                return pygame.image.load(filename).convert_alpha()
            except pygame.error:
                return None
        return None

    def get_screen_coords(self):
        width = math.sqrt(3) * self.size
        height = 2 * self.size
        pos_x = self.grid_x * width
        pos_y = self.grid_y * (height * 0.75)
        if self.grid_y % 2 == 1:
            pos_x += width / 2
        return pos_x, pos_y