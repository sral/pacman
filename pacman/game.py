import sys
import pygame

from maze import Maze
from pacman import PacMan
from tileset import Tileset


__author__ = 'Lars Djerf <lars.djerf@gmail.com'

HORIZONTAL_TILES = 28
VERTICAL_TILES = 36
TILE_WIDTH = 8
TILE_HEIGHT = 8
SPRITE_WIDTH = 16
SPRITE_HEIGHT = 16
SCREEN_WIDTH = 224  # 28 * 8 px
SCREEN_HEIGHT = 288  # 36 * 8 px


class Game(object):
    def __init__(self):
        self.maze_tiles = None
        self.pacman_tiles = None

    @staticmethod
    def tile_to_screen(x, y):
        """Returns tile bounding box (screen coordinates).

        Keyword argument(s):
        tile -- Tile coordinates (x, y)
        """

        x *= TILE_WIDTH
        y *= TILE_HEIGHT

        return x, y, x + TILE_WIDTH - 1, y + TILE_HEIGHT - 1

    @staticmethod
    def screen_to_tile(x, y):
        """Convert screen coordinate/point to tile/maze coordinate.

        Keyword argument(s):
        coordinate -- Screen coordinate (x, y)

        Returns tile coordinate.
        """

        # This is weird, no?
        # Should be:
        # return x / TILE_WIDTH, y / TILE_HEIGHT

        return (x / TILE_WIDTH) + 1, (y / TILE_HEIGHT) + 1

    @staticmethod
    def is_aligned(coordinate):
        """Check if coordinate is aligned with tile border.

        Keyword argument(s):
        coordinate -- Coordinate to check

        Returns True if aligned, False otherwise.
        """

        return (coordinate + 4) % 8 == 0

    def get_sprite_bounding_box(self, sprite):
        """Returns sprite bounding box.

        Keyword argument(s):
        sprite -- The sprite
        """

        return (sprite.x, sprite.y, sprite.x + SPRITE_WIDTH - 1,
                sprite.y + SPRITE_HEIGHT - 1)


    def setup(self):
        """Setup game."""

        pygame.init()
        pygame.display.set_caption("pacman")
        self.maze_tiles = Tileset("data/tiles.gif", TILE_WIDTH, TILE_HEIGHT)
        self.pacman_tiles = Tileset("data/pacman.gif", SPRITE_WIDTH,
                                    SPRITE_HEIGHT)

    def write_message(self, x, y, message):
        """Write message.

        Keyword arguments:
        x -- x-coordinate
        y -- y-coordinate
        message -- Message to write
        """

        for i, char in enumerate(message):
            self.maze_tiles.draw(x + i, y, ord(char))

    def legal_move(self, maze, sprite, delta):
        """Check if move is collision.

        Keyword argument(s):
        maze -- Maze/playfield
        sprite -- Sprite to move
        delta -- Delta tuple (x, y)

        Returns True if the move is collision, False otherwise.
        """

        x, y = self.screen_to_tile(sprite.x + delta[0], sprite.y + delta[1])
        next_tile_type = maze[(x + delta[0], y + delta[1])]
        collision = False

        if next_tile_type > 3:  # > 3 is wall type
            x0, y0, x1, y1 = self.tile_to_screen(x, y)
            x2, y2, x3, y3 = self.get_sprite_bounding_box(sprite)
            if delta[0] > 0 and x3 >= x1 + 4:  # Right
                collision = True
            elif delta[0] < 0 and x2 - 1 < x0 - 4:  # Left
                collision = True
            elif delta[1] > 0 and y3 - 4 >= y1:  # Down
                collision = True
            elif delta[1] < 0 and y2 + 4 <= y0:  # Up
                collision = True

        aligned = False
        if delta[0] != 0:  # left/right align y
            aligned = self.is_aligned(sprite.y)
        elif delta[1] != 0:  # up/down align x
            aligned = self.is_aligned(sprite.x)

        return aligned and not collision

    def game_loop(self):
        """Main loop. """

        pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        score = 0
        high_score = 0
        maze = Maze(self.maze_tiles, HORIZONTAL_TILES, VERTICAL_TILES)
        maze.load_level(maze.MAZE)
        pac = PacMan(104, 204, self.pacman_tiles)
        delta = (0, 0)
        while True:
            event = pygame.event.poll()
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    sys.exit(0)

            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_LEFT]:
                delta = (-1, 0)
            elif pressed[pygame.K_RIGHT]:
                delta = (1, 0)
            elif pressed[pygame.K_DOWN]:
                delta = (0, 1)
            elif pressed[pygame.K_UP]:
                delta = (0, -1)

            x, y = self.screen_to_tile(pac.x, pac.y)
            if maze[(x, y)] > 0:
                score += 10
                maze[(x, y)] = 0
                if score > high_score:
                    high_score = score

            if self.legal_move(maze, pac, delta):
                pac.delta = delta
            elif not self.legal_move(maze, pac, pac.delta):
                pac.delta = (0, 0)

            pac.move()
            maze.draw()
            pac.draw()
            self.write_message(3, 0, "1UP")
            self.write_message(4, 1, str(score))
            self.write_message(9, 0, "HIGH SCORE")
            self.write_message(10, 1, str(score))
            pygame.display.flip()


def main():
    p = Game()
    p.setup()
    p.game_loop()


if __name__ == "__main__":
    main()