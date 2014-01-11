__author__ = 'Lars Djerf <lars.djerf@gmail.com'

MAX_FRAME = 8  # number of frames in animation


class PacMan(object):
    def __init__(self, x, y, sprites):
        """Initialize instance."""

        self.x = x
        self.y = y
        self.delta = (0, 0)
        self.frame = 0
        self.tiles = sprites


    def move(self):
        """Move Pac-Man."""

        self.x += self.delta[0]
        self.y += self.delta[1]
        self.frame = (self.frame + 1) % MAX_FRAME  # add direction


    def draw(self):
        """Draw current frame."""

        self.tiles.draw_surface(self.x, self.y, self.frame)
