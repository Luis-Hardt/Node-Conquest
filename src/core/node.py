import math

SQRT3_2 = math.sqrt(3) / 2

class Node:
    def __init__(self, x, y, width=64, height=64, weight=1):
        self.grid_x = x
        self.grid_y = y
        self.width = width
        self.height = height
        self.owner = None
        self.weight = weight
        self.move_cost = weight
        self.color = self._get_color(weight)

    def set_weight(self, weight):
        self.weight = weight
        if self.owner is None:
            self.move_cost = weight
            self.color = self._get_color(weight)

    def capture(self, player):
        if self.owner is None:
            player.points += self.weight
            self.owner = player
            self.move_cost = 0
            self.color = player.color
            return True
        return False

    def _get_color(self, weight):
        shades = {
            1: (235, 235, 235),
            2: (180, 180, 180),
            3: (120, 120, 120)
        }
        return shades.get(weight, (255, 255, 255))

    def get_screen_coords(self):
        pos_x = self.grid_x * (self.width * SQRT3_2)
        pos_y = self.grid_y * (self.height * 0.75)
        if self.grid_y % 2 == 1:
            pos_x += (self.width * SQRT3_2) * 0.5
        return pos_x, pos_y