import pygame
import sys
from EventHandler import EventHandler
from Player import Player
from Camera import Camera
from Walls import Walls
from Enemies import Enemy  # Import Enemy class

# Initialize Pygame
pygame.init()

# Set up the window
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Window")

event_handler = EventHandler()
camera = Camera(WIDTH, HEIGHT)
player = Player(WIDTH // 2, HEIGHT // 2, camera)


# Create a box of walls 3x the size of the screen around the player
walls = Walls()
box_width = WIDTH * 3
box_height = HEIGHT * 3
box_x = player.x - box_width // 2
box_y = player.y - box_height // 2
wall_thickness = 40

# Top wall
walls.add_wall(box_x, box_y, box_width, wall_thickness)
# Bottom wall
walls.add_wall(box_x, box_y + box_height - wall_thickness, box_width, wall_thickness)
# Left wall
walls.add_wall(box_x, box_y, wall_thickness, box_height)
# Right wall
walls.add_wall(box_x + box_width - wall_thickness, box_y, wall_thickness, box_height)

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

# --- Add a couple of enemy entities ---
enemies = [
    Enemy(player.x + 200, player.y, speed=2),
    Enemy(player.x - 250, player.y + 100, speed=2)
]


# Main loop
clock = pygame.time.Clock()
running = True
while running:
    draw_checkerboard(screen, camera, WIDTH, HEIGHT)  # Draw checkerboard background
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