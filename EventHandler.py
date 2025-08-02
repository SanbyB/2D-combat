import pygame
import sys

class EventHandler:
    def __init__(self):
        self.keys = {'w': False, 'a': False, 's': False, 'd': False}
        self.mouse_pos = (0, 0)
        self.mouse_buttons = {1: False, 2: False, 3: False}  # 1: left, 2: middle, 3: right
        self.scroll = 0  # Positive for up, negative for down

    def process_events(self):
        self.scroll = 0  # Reset scroll each frame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False  # Quit event, signal to stop main loop

            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                is_down = event.type == pygame.KEYDOWN
                if event.key == pygame.K_w:
                    self.keys['w'] = is_down
                if event.key == pygame.K_a:
                    self.keys['a'] = is_down
                if event.key == pygame.K_s:
                    self.keys['s'] = is_down
                if event.key == pygame.K_d:
                    self.keys['d'] = is_down

            if event.type == pygame.MOUSEMOTION:
                self.mouse_pos = event.pos

            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
                is_down = event.type == pygame.MOUSEBUTTONDOWN
                if event.button in self.mouse_buttons:
                    self.mouse_buttons[event.button] = is_down
                if event.button == 4:  # Scroll up
                    self.scroll = 1
                if event.button == 5:  # Scroll down
                    self.scroll = -1

        return True  # Continue running if no quit event


