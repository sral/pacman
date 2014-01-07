from unittest import TestCase

from pacman.maze import Maze

__author__ = 'Lars Djerf <lars.djerf@gmail.com'


class TestMaze(TestCase):
    def test_load_level(self):
        """Maze should reflect the tile map.

        1.) Load tile map
        2.) Compare maze to tile map
        => Maze should reflect tile map i.e. correct value at correct
           coordinates."""

        maze = Maze(None)
        maze.load_level(maze.MAZE)
        for y in range(maze.height):
            for x in range(maze.width):
                self.assertEqual(maze[(x, y)], maze.MAZE[y * maze.width + x])


    def test_set_tile(self):
        """Maze should support altering values.

        1.) Update value/object in maze
        =>  Value is updated."""

        tile_map = [1, 2, 3, 4, 5]

        maze = Maze(None)
        maze.load_level(tile_map)
        for x, v in enumerate(reversed(tile_map)):
            maze[(x, 0)] = v
            self.assertEqual(maze[(x, 0)], v)

    def test_index_error_if_get_out_of_bounds(self):
        """Maze should raise IndexError if coordinates are illegal.

        1.) Read value outside of maze
        => IndexError is raised."""

        illegal_values = ((-1, 0),
                          (0, -1),
                          (0, 36),
                          (28, 0),
                          (28, 36))

        maze = Maze(None)
        for coordinates in illegal_values:
            with self.assertRaises(IndexError):
                tmp = maze[coordinates]


    def test_index_error_if_set_out_of_bounds(self):
        """Maze should raise IndexError if coordinates are illegal.

        1.) Write value outside of maze
        => IndexError is raised."""

        illegal_values = ((-1, 0),
                          (0, -1),
                          (0, 36),
                          (28, 0),
                          (28, 36))

        maze = Maze(None)
        for coordinates in illegal_values:
            with self.assertRaises(IndexError):
                maze[coordinates] = 1


