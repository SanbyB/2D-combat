import random
import pygame
from Animation import Animation
from Entity import Entity

class Enemy(Entity):
    def __init__(self, x, y, radius=18, color=(200, 50, 50), speed=2, chase_radius=250):
        super().__init__(x, y, radius, color, speed)
        self.chase_radius = chase_radius
        self.attack_distance = 100  # Distance at which the enemy can attack

        size = 64
        scale = 1.2

        self.base_animation = Animation("Graphics/idleEnemy.png", size, size, 2, speed=random.randint(20, 30), scale=scale)  # Load enemy animation
        self.animation = self.base_animation  # Set base animation for idle state
        
        self.radius = size * scale / 2  # Adjust radius based on sprite size and scale


    def update(self, player, walls=None, entities=None):
        # Calculate distance to player
        dx = player.x - self.x
        dy = player.y - self.y
        distance = (dx ** 2 + dy ** 2) ** 0.5

        # Only move toward player if within chase radius
        if distance < self.chase_radius and distance != 0:
            # Normalize direction
            dx /= distance
            dy /= distance
            self.move(dx * self.speed, dy * self.speed, walls, entities)

        self.attack(distance, player)
        self.update_attack_cooldown()

        # Handle flash timer for damage feedback
        if self.flash_timer > 0:
            self.flash_timer -= 1
            if self.flash_timer == 0:
                self.color = self.base_color
                self.animation = self.base_animation

    def take_damage(self, amount):
        self.health -= amount
        self.animation = Animation("Graphics/damageEnemy.png", 64, 64, 1, speed=random.randint(20, 30), scale=1.2)
        self.color = (255, 255, 255)  # Flash white
        self.flash_timer = 5  # Number of frames to stay white

    def attack(self, distance, player):
        if not super().attack():
            return False
        
        if distance <= self.attack_distance:
            player.take_damage(self.attack_strength)

        