__author__ = 'Lars Djerf <lars.djerf@gmail.com'


class Maze(object):
    MAZE = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 23, 24, 9, 9, 9, 9, 9, 9, 9, 9,
            9, 9, 9, 9, 4, 7, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 19, 20, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 8, 7, 1,
            15, 21, 21, 16, 1, 15, 21, 21, 21, 16, 1, 19, 20, 1, 15, 21, 21, 21, 16, 1, 15, 21, 21, 16, 1, 8, 7, 2, 19,
            0, 0, 20, 1, 19, 0, 0, 0, 20, 1, 19, 20, 1, 19, 0, 0, 0, 20, 1, 19, 0, 0, 20, 2, 8, 7, 1, 17, 22, 22, 18, 1,
            17, 22, 22, 22, 18, 1, 17, 18, 1, 17, 22, 22, 22, 18, 1, 17, 22, 22, 18, 1, 8, 7, 1, 1, 1, 1, 1, 1, 1, 1, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 8, 7, 1, 15, 21, 21, 16, 1, 15, 16, 1, 15, 21, 21, 21,
            21, 21, 21, 16, 1, 15, 16, 1, 15, 21, 21, 16, 1, 8, 7, 1, 17, 22, 22, 18, 1, 19, 20, 1, 17, 22, 22, 28, 27,
            22, 22, 18, 1, 19, 20, 1, 17, 22, 22, 18, 1, 8, 7, 1, 1, 1, 1, 1, 1, 19, 20, 1, 1, 1, 1, 19, 20, 1, 1, 1, 1,
            19, 20, 1, 1, 1, 1, 1, 1, 8, 5, 10, 10, 10, 10, 16, 1, 19, 29, 21, 21, 16, 0, 19, 20, 0, 15, 21, 21, 30, 20,
            1, 15, 10, 10, 10, 10, 6, 0, 0, 0, 0, 0, 7, 1, 19, 27, 22, 22, 18, 0, 17, 18, 0, 17, 22, 22, 28, 20, 1, 8,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 1, 19, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 19, 20, 1, 8, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 7, 1, 19, 20, 0, 25, 10, 10, 95, 95, 10, 10, 26, 0, 19, 20, 1, 8, 0, 0, 0, 0, 0, 9, 9, 9, 9, 9, 18,
            1, 17, 18, 0, 8, 0, 0, 0, 0, 0, 0, 7, 0, 17, 18, 1, 17, 9, 9, 9, 9, 9, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 8, 0,
            0, 0, 0, 0, 0, 7, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 10, 10, 10, 10, 10, 16, 1, 15, 16, 0, 8, 0, 0, 0, 0, 0, 0,
            7, 0, 15, 16, 1, 15, 10, 10, 10, 10, 10, 0, 0, 0, 0, 0, 7, 1, 19, 20, 0, 31, 9, 9, 9, 9, 9, 9, 38, 0, 19,
            20, 1, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 1, 19, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 19, 20, 1, 8, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 7, 1, 19, 20, 0, 15, 21, 21, 21, 21, 21, 21, 16, 0, 19, 20, 1, 8, 0, 0, 0, 0, 0, 3, 9,
            9, 9, 9, 18, 1, 17, 18, 0, 17, 22, 22, 28, 27, 22, 22, 18, 0, 17, 18, 1, 17, 9, 9, 9, 9, 4, 7, 1, 1, 1, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 19, 20, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 8, 7, 1, 15, 21, 21, 16, 1, 15, 21, 21,
            21, 16, 1, 19, 20, 1, 15, 21, 21, 21, 16, 1, 15, 21, 21, 16, 1, 8, 7, 1, 17, 22, 28, 20, 1, 17, 22, 22, 22,
            18, 1, 17, 18, 1, 17, 22, 22, 22, 18, 1, 19, 27, 22, 18, 1, 8, 7, 2, 1, 1, 19, 20, 1, 1, 1, 1, 1, 1, 1, 0,
            0, 1, 1, 1, 1, 1, 1, 1, 19, 20, 1, 1, 2, 8, 12, 21, 16, 1, 19, 20, 1, 15, 16, 1, 15, 21, 21, 21, 21, 21, 21,
            16, 1, 15, 16, 1, 19, 20, 1, 15, 21, 14, 11, 22, 18, 1, 17, 18, 1, 19, 20, 1, 17, 22, 22, 28, 27, 22, 22,
            18, 1, 19, 20, 1, 17, 18, 1, 17, 22, 13, 7, 1, 1, 1, 1, 1, 1, 19, 20, 1, 1, 1, 1, 19, 20, 1, 1, 1, 1, 19,
            20, 1, 1, 1, 1, 1, 1, 8, 7, 1, 15, 21, 21, 21, 21, 30, 29, 21, 21, 16, 1, 19, 20, 1, 15, 21, 21, 30, 29, 21,
            21, 21, 21, 16, 1, 8, 7, 1, 17, 22, 22, 22, 22, 22, 22, 22, 22, 18, 1, 17, 18, 1, 17, 22, 22, 22, 22, 22,
            22, 22, 22, 18, 1, 8, 7, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 8, 5,
            10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 6,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def __init__(self, tileset):
        """Initialize instance.

        Keyword argument(s):
        tileset -- Tileset instance
        """
        self.width = 28
        self.height = 36
        self.tiles = tileset
        self.maze = {}  # Matrix

    def load_level(self, tile_map):
        """Load map.

        Keyword argument(s):
        tile_map -- Tile map
        """

        x = y = 0
        for tile in tile_map:
            self.maze[(x, y)] = tile
            if x >= self.width - 1:  # pacman.HORIZONTAL_TILES - 1
                x = 0
                y += 1
            else:
                x += 1

    def draw(self):
        """Draw maze."""

        for coordinates, tile in self.maze.iteritems():
            x, y = coordinates
            self.tiles.draw(x, y, tile)

    def __getitem__(self, key):
        """Returns maze tile at coordinates.

        Keyword arguments:
        key -- Tuple containing tile coordinates
        """

        x, y = key
        if (x < 0 or x >= self.width or
                    y < 0 or
                    y >= self.height):
            raise IndexError("Illegal tile coordinates: (%d, %d)." % (x, y))
        return self.maze.get(key, 0)

    def __setitem__(self, key, value):
        """Set tile in playfield.

        Keyword arguments:
        key -- Tuple containing tile coordinates
        value -- Tile type
        """

        x, y = key
        if (x < 0 or x >= self.width or
                    y < 0 or y >= self.height):
            raise IndexError("Illegal tile coordinates: (%d, %d)." % (x, y))
        self.maze[key] = value
