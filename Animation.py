import pygame

class Animation:
    def __init__(self, image_path, frame_width, frame_height, num_frames, speed=5, scale=1.0):
        """
        image_path: path to the sprite sheet PNG
        frame_width: width of each frame in pixels
        frame_height: height of each frame in pixels
        num_frames: total number of frames in the animation
        speed: number of game frames to wait before advancing to next sprite frame
        """
        self.sprite_sheet = pygame.image.load(image_path).convert_alpha()
        self.frame_width = frame_width
        self.frame_height = frame_height
        self.num_frames = num_frames
        self.speed = speed
        self.current_frame = 0
        self.frame_counter = 0
        self.scale = scale

        # Extract frames from the sprite sheet
        self.frames = []
        for i in range(num_frames):
            rect = pygame.Rect(i * frame_width, 0, frame_width, frame_height)
            frame = self.sprite_sheet.subsurface(rect)
            self.frames.append(frame)

    def update(self):
        # Advance the animation based on speed
        self.frame_counter += 1
        if self.frame_counter >= self.speed:
            self.current_frame = (self.current_frame + 1) % self.num_frames
            self.frame_counter = 0

    def draw(self, surface, pos):
        """
        surface: pygame.Surface to draw on
        pos: (x, y) tuple for the top-left position to draw the frame
        scale: float, scale factor for the frame size
        """
        frame = self.frames[self.current_frame]
        frame_pos = (pos[0] - self.frame_width * self.scale // 2, pos[1] - self.frame_height * self.scale // 2)
        if self.scale != 1.0:
            new_size = (int(self.frame_width * self.scale), int(self.frame_height * self.scale))
            frame = pygame.transform.scale(frame, new_size)
        surface.blit(frame, frame_pos)