__author__ = 'Lars Djerf <lars.djerf@gmail.com'

MAX_FRAME = 2  # number of frames in animation
FRAME_INDEX = {(1, 0): 0 * MAX_FRAME,
               (-1, 0): 1 * MAX_FRAME,
               (0, 1): 2 * MAX_FRAME,
               (0, -1): 3 * MAX_FRAME}

class PacMan(object):
    def __init__(self, x, y, frames):
        """Initialize instance."""

        self.x = x
        self.y = y
        self.delta = (0, 0)
        self.frame = 0
        self.frames = frames

    def move(self):
        """Move Pac-Man."""

        if self.delta != (0, 0):
            self.x += self.delta[0]
            self.y += self.delta[1]
            self.frame = FRAME_INDEX[self.delta] + (self.frame + 1) % MAX_FRAME

    def draw(self):
        """Draw current frame."""

        self.frames.draw_surface(self.x, self.y, self.frame)
