import pygame
import sys
from EventHandler import EventHandler
from Player import Player
from Camera import Camera

# Initialize Pygame
pygame.init()

# Set up the window
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Window")

event_handler = EventHandler()
player = Player(WIDTH // 2, HEIGHT // 2)
camera = Camera(WIDTH, HEIGHT)

def draw_checkerboard(surface, camera, width, height, tile_size=40, color1=(50, 50, 50), color2=(80, 80, 80)):
    # Draw enough tiles to cover the visible area, offset by camera
    start_x = (camera.offset_x // tile_size) * tile_size
    start_y = (camera.offset_y // tile_size) * tile_size
    end_x = camera.offset_x + width
    end_y = camera.offset_y + height

    for y in range(int(start_y), int(end_y), tile_size):
        for x in range(int(start_x), int(end_x), tile_size):
            if ((x // tile_size + y // tile_size) % 2) == 0:
                color = color1
            else:
                color = color2
            rect_x, rect_y = camera.apply((x, y))
            pygame.draw.rect(surface, color, (rect_x, rect_y, tile_size, tile_size))

# Main loop
clock = pygame.time.Clock()
running = True
while running:
    running = event_handler.process_events()

    player.update(event_handler.keys)
    camera.update(player.x, player.y)

    draw_checkerboard(screen, camera, WIDTH, HEIGHT)  # Draw checkerboard background
    # Draw player at camera-adjusted position
    player_screen_pos = camera.apply((player.x, player.y))
    player.draw_at(screen, player_screen_pos)
    pygame.display.flip()

    clock.tick(60)  # Limit to 60 frames per second

# Clean up
pygame.quit()
sys.exit()