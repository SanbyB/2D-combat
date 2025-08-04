import pygame
from Animation import Animation
from Entity import Entity

class Player(Entity):
    def __init__(self, x, y, camera=None, radius=15, color=(0, 200, 255), speed=4):
        super().__init__(x, y, radius, color, speed)
        self.camera = camera

        size = 64
        scale = 1.2

        self.radius = size * scale / 2  # Adjust radius based on sprite size and scale

        self.animations = {
            'idle': Animation("Graphics/idle.png", size, size, 2, speed=30, scale=scale),
            'walking': Animation("Graphics/walking.png", size, size, 3, speed=15, scale=scale),
            'damage': Animation("Graphics/damage.png", size, size, 1, speed=25, scale=scale)
        }

        self.animation = self.animations['idle']

    def update(self, keys, mouse_buttons, mouse_pos, walls=None, enemies=None):
        dx, dy = 0, 0
        if keys['w']:
            dy -= 1
        if keys['s']:
            dy += 1
        if keys['a']:
            dx -= 1
            self.facingRight = False
        if keys['d']:
            dx += 1
            self.facingRight = True

        # Normalize movement to prevent faster diagonal movement
        if dx != 0 or dy != 0:
            self.move(dx * self.speed, dy * self.speed, walls, enemies)
            self.animation = self.animations['walking']
        else:
            self.animation = self.animations['idle']

        if mouse_buttons[1]:
            self.attack(mouse_pos, enemies)
        self.update_attack_cooldown()

        # Handle flash timer for damage feedback
        if self.flash_timer > 0:
            self.animation = self.animations['damage']
            self.flash_timer -= 1
            if self.flash_timer == 0:
                self.animation = self.animations['idle']
                self.color = self.base_color

    def take_damage(self, amount):
        self.health -= amount
        self.color = (255, 255, 255)  # Flash white
        self.flash_timer = 5  # Number of frames to stay white

    def attack(self, mouse_pos, enemies):
        if not super().attack():
            return False

        for enemy in enemies:
            if enemy is self:
                continue

            # Calculate distance to enemy
            dx = enemy.x - self.x
            dy = enemy.y - self.y
            distance = (dx ** 2 + dy ** 2) ** 0.5

            if distance <= self.attack_distance:
                x, y = self.camera.apply((enemy.rect.x, enemy.rect.y))
                entRect = pygame.Rect(
                    x,
                    y,
                    enemy.rect.width,
                    enemy.rect.height
                )
                if entRect.collidepoint(mouse_pos):
                    enemy.take_damage(self.attack_strength)
                    if enemy.health <= 0:
                        enemies.remove(enemy)