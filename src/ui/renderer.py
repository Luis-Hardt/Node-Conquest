import pygame
import math

class Renderer:
    def __init__(self, screen, camera_offset=(0, 0)):
        self.screen = screen
        self.camera_offset = list(camera_offset)

    def set_camera(self, x, y):
        self.camera_offset[0] = x
        self.camera_offset[1] = y

    def move_camera(self, dx, dy):
        self.camera_offset[0] += dx
        self.camera_offset[1] += dy

    def render_graph(self, graph):
        for node in graph.nodes.values():
            self.draw_node(node)

    def draw_node(self, node):
        base_x, base_y = node.get_screen_coords()
        draw_x = base_x + self.camera_offset[0]
        draw_y = base_y + self.camera_offset[1]

        if isinstance(node.sprite, pygame.Surface):
            self.screen.blit(node.sprite, (draw_x, draw_y))
        else:
            self._draw_hex_outline(node, draw_x, draw_y)

    def _draw_hex_outline(self, node, center_x, center_y):
        points = []
        for i in range(6):
            angle_deg = 60 * i - 30
            angle_rad = math.pi / 180 * angle_deg
            px = center_x + node.size * math.cos(angle_rad)
            py = center_y + node.size * math.sin(angle_rad)
            points.append((px, py))
        
        pygame.draw.polygon(self.screen, node.color, points)
        pygame.draw.polygon(self.screen, (150, 150, 150), points, 1)

    def clear(self, color=(30, 30, 30)):
        self.screen.fill(color)