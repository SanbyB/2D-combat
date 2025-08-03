import pygame
import sys
from EventHandler import EventHandler
from Camera import Camera
from MapLoader import MapLoader
from utils import draw_checkerboard

# Initialize Pygame
pygame.init()

# Set up the window
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Window")

event_handler = EventHandler()
camera = Camera(WIDTH, HEIGHT)

# Load map and entities
map_loader = MapLoader()
walls, enemies, player = map_loader.load("Graphics/map.png")  # Replace with your map
player.camera = camera  # Set the player's camera


# Main loop
clock = pygame.time.Clock()
running = True
while running:
    # draw_checkerboard(screen, camera, WIDTH, HEIGHT)  # Draw checkerboard background
    pygame.draw.rect(screen, (39, 39, 68), (0, 0, WIDTH, HEIGHT))  # Clear screen with black
    walls.draw(screen, camera)  # Draw walls
    running = event_handler.process_events()

    for enemy in enemies:
        enemy.update(player, walls, enemies + [player])
        # Draw enemies
        enemy_screen_pos = camera.apply((enemy.x, enemy.y))
        enemy.draw_at(screen, enemy_screen_pos)

    camera.update(player.x, player.y)   

    player.update(event_handler.keys, event_handler.mouse_buttons, event_handler.mouse_pos, walls, enemies)

    # Draw player at camera-adjusted position
    player_screen_pos = camera.apply((player.x, player.y))
    player.draw_at(screen, player_screen_pos)
    pygame.display.flip()

    clock.tick(60)  # Limit to 60 frames per second

# Clean up
pygame.quit()
sys.exit()