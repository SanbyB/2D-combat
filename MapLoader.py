import pygame
from Walls import Walls
from Player import Player
from Enemies import Enemy

class MapLoader:
    def __init__(self, color_map=None):
        # Define color to entity/wall mapping
        # Format: (R, G, B): ("type", kwargs)
        self.color_map = color_map or {
            (255, 0, 0): ("wall", {}),                # Red = Wall
            (0, 255, 0): ("player", {}),            # Green = Player
            (0, 0, 255): ("enemy", {}),             # Blue = Enemy
            # Add more mappings as needed
        }

    def load(self, filename):
        image = pygame.image.load(filename)
        image = image.convert()  # Ensure pixel format
        width, height = image.get_size()

        walls = Walls()
        entities = []
        player = None

        for y in range(height):
            for x in range(width):
                color = image.get_at((x, y))[:3]  # Ignore alpha
                if color in self.color_map:
                    obj_type, kwargs = self.color_map[color]
                    world_x, world_y = x * 40, y * 40  # 40 is tile size, adjust as needed

                    if obj_type == "wall":
                        walls.add_wall(world_x, world_y, 40, 40)
                    elif obj_type == "player":
                        player = Player(world_x + 20, world_y + 20)  # Center in tile
                    elif obj_type == "enemy":
                        entities.append(Enemy(world_x + 20, world_y + 20))
                    # Add more types as needed

        return walls, entities, player