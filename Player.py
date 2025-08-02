import pygame
from Entity import Entity

class Player(Entity):
    def __init__(self, x, y, radius=20, color=(0, 200, 255), speed=3):
        super().__init__(x, y, radius, color, speed)

    def update(self, keys, walls=None):
        dx, dy = 0, 0
        if keys['w']:
            dy -= 1
        if keys['s']:
            dy += 1
        if keys['a']:
            dx -= 1
        if keys['d']:
            dx += 1

        # Normalize movement to prevent faster diagonal movement
        if dx != 0 or dy != 0:
            self.move(dx * self.speed, dy * self.speed, walls)

    def draw_at(self, surface, pos):
        pygame.draw.circle(surface, self.color, (int(pos[0]), int(pos[1])), self.radius)

