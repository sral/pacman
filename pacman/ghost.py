__author__ = 'Lars Djerf <lars.djerf@gmail.com'


class Ghost(object):
    def __init__(self, x, y, sprites):
        """Initialize instance.

        Keyword argument(s):
        x --
        y --
        sprites --
        """
        self.x = x
        self.y = y
        self.scatter = False
        self.target_tile = None
        self.sprites = sprites

    def move(self):
        """Move ghost."""

        pass

    def draw(self):
        pass