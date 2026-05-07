import pygame
import random
from core.graph import Graph
from ui.renderer import Renderer

def main():
    pygame.init()
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Hex Grid Generator")
    clock = pygame.time.Clock()

    grid_width = 10
    grid_height = 10
    tile_size = 30
    terrains = ["plain", "forest", "hills", "forest_hills", "water"]

    game_map = Graph(grid_width, grid_height, tile_size)
    
    for node in game_map.nodes.values():
        random_terrain = random.choice(terrains)
        node.terrain_type = random_terrain
        node.color = node._set_color(random_terrain)
        node.move_cost = node._set_cost(random_terrain)
        node.sprite = node._set_sprite(random_terrain)

    renderer = Renderer(screen, camera_offset=(50, 50))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        renderer.clear((20, 20, 20))
        renderer.render_graph(game_map)
        
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()