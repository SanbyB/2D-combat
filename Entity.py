import pygame
import math

class Entity:
    def __init__(self, x, y, radius=20, color=(255, 255, 255), speed=3, max_health=100):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed = speed
        self.attack_cooldown = 0  # Frames until next attack allowed
        self.attack_speed = 50    # Frames between attacks
        self.attack_strength = 10
        self.attack_distance = 150
        self.health = max_health  # Health attribute
        self.max_health = max_health

        self.base_color = color
        self.flash_timer = 0

    @property
    def rect(self):
        # Returns a pygame.Rect representing the entity's collision bounds
        return pygame.Rect(
            self.x - self.radius,
            self.y - self.radius,
            self.radius * 2,
            self.radius * 2
        )

    def move(self, dx, dy, walls, entities=None):
        # Normalize movement to prevent faster diagonal movement
        if dx != 0 or dy != 0:
            length = (dx ** 2 + dy ** 2) ** 0.5
            dx /= length
            dy /= length

            dx *= self.speed
            dy *= self.speed

        original_x, original_y = self.x, self.y

        # Move in x direction and check collision
        self.x += dx
        if (walls and walls.check_collision(self.rect)) or (entities and self.check_entity_collision(entities)):
            self.x = original_x  # Undo x move if colliding

        # Move in y direction and check collision
        self.y += dy
        if (walls and walls.check_collision(self.rect)) or (entities and self.check_entity_collision(entities)):
            self.y = original_y  # Undo y move if colliding

    def check_entity_collision(self, entities):
        """Returns True if this entity collides with any other entity in the list."""
        for entity in entities:
            if entity is self:
                continue
            if self.rect.colliderect(entity.rect):
                return True
        return False

    def attack(self):
        if self.attack_cooldown > 0:
            return  False # Still in cooldown

        self.attack_cooldown = self.attack_speed  # Reset cooldown
        return True

    def update_attack_cooldown(self):
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1

    def draw_at(self, surface, pos):
        # when changing this with a sprite make sure to move the position to the center of the entity
        pygame.draw.circle(surface, self.color, (int(pos[0]), int(pos[1])), self.radius)

        # Draw health bar above the entity
        bar_width = self.radius * 2
        bar_height = 6
        health_ratio = max(self.health, 0) / self.max_health
        bar_x = int(pos[0] - self.radius)
        bar_y = int(pos[1] - self.radius - bar_height - 4)

        # Background (red)
        pygame.draw.rect(surface, (120, 0, 0), (bar_x, bar_y, bar_width, bar_height))
        # Foreground (green)
        pygame.draw.rect(surface, (0, 200, 0), (bar_x, bar_y, bar_width * health_ratio, bar_height))