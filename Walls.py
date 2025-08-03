import pygame

class Wall:
    def __init__(self, x, y, width, height, color=(120, 120, 120)):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color

    def draw(self, surface, camera):
        # Draw wall at camera-adjusted position
        screen_pos = camera.apply((self.rect.x, self.rect.y))
        pygame.draw.rect(surface, self.color, (screen_pos[0], screen_pos[1], self.rect.width, self.rect.height))

class Walls:
    def __init__(self):
        self.walls = []

    def add_wall(self, x, y, width, height, color=(0,0,0)):
        self.walls.append(Wall(x, y, width, height, color))

    def draw(self, surface, camera):
        for wall in self.walls:
            wall.draw(surface, camera)

    def get_rects(self):
        return [wall.rect for wall in self.walls]

    def check_collision(self, rect):
        """Returns True if rect collides with any wall."""
        for wall_rect in self.get_rects():
            if rect.colliderect(wall_rect):
                return True
        return False