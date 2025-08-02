import pygame

class Entity:
    def __init__(self, x, y, radius=20, color=(255, 255, 255), speed=3):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed = speed

    @property
    def rect(self):
        # Returns a pygame.Rect representing the entity's collision bounds
        return pygame.Rect(
            self.x - self.radius,
            self.y - self.radius,
            self.radius * 2,
            self.radius * 2
        )

    def move(self, dx, dy, walls):
        # Attempt to move and resolve collisions with walls
        original_x, original_y = self.x, self.y

        length = (dx ** 2 + dy ** 2) ** 0.5
        if length != 0:
            dx /= length
            dy /= length

        # Move in x direction and check collision
        self.x += dx
        if walls and walls.check_collision(self.rect):
            self.x = original_x  # Undo x move if colliding

        # Move in y direction and check collision
        self.y += dy
        if walls and walls.check_collision(self.rect):
            self.y = original_y  # Undo y move if colliding
        

    def draw_at(self, surface, pos):
        pygame.draw.circle(surface, self.color, (int(pos[0]), int(pos[1])), self.radius)