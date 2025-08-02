class Camera:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.offset_x = 0
        self.offset_y = 0

    def update(self, target_x, target_y):
        # Center the camera on the target (e.g., player)
        self.offset_x = target_x - self.width // 2
        self.offset_y = target_y - self.height // 2

    def apply(self, pos):
        # Adjust a position by the camera offset
        x, y = pos
        return x - self.offset_x, y - self.offset_y