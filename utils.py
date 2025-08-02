import pygame

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
