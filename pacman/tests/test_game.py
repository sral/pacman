from unittest import TestCase
from pacman.game import Game, HORIZONTAL_TILES, VERTICAL_TILES
from pacman.game import SCREEN_WIDTH, SCREEN_HEIGHT
from pacman.game import TILE_WIDTH, TILE_HEIGHT


__author__ = 'Lars Djerf <lars.djerf@gmail.com'


class TestGame(TestCase):

    def test_tile_to_screen(self):
        """Tile coordinates should map to correct screen coordinates."""

        for y in range(HORIZONTAL_TILES):
            for x in range(VERTICAL_TILES):
                x0 = x * TILE_WIDTH
                y0 = y * TILE_HEIGHT
                x1 = x0 + TILE_WIDTH
                y1 = y0 + TILE_HEIGHT
                self.assertEqual(Game.tile_to_screen(x, y),
                                 (x0, y0, x1, y1))


    def test_screen_to_tile(self):
        """Screen coordinates should map to correct tile coordinates."""

        for y in range(SCREEN_HEIGHT):
            for x in range(SCREEN_WIDTH):
                self.assertEqual(Game.screen_to_tile(x, y),
                                 (x / HORIZONTAL_TILES, y / VERTICAL_TILES))
