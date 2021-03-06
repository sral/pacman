import pkg_resources
import pygame

__author__ = 'Lars Djerf <lars.djerf@gmail.com'

class Tileset(object):

    def __init__(self, image, tile_width, tile_height):
        """Initialize instance.

        Keyword arguments:
        image -- Bitmap containing maze_tiles
        tile_width -- Tile width
        tile_height -- Tile height
        """

        self.tile_width = tile_width
        self.tile_height = tile_height
        self.tiles = {}

        image = pkg_resources.resource_filename(__name__, image)
        image = pygame.image.load(image)
        for i in range(image.get_width() / tile_width):
            area = pygame.Rect(i * tile_width, 0, tile_width, tile_height)
            tile = pygame.Surface((tile_width, tile_height))
            tile.blit(image, (0, 0), area)
            self.tiles[i] = tile

    def draw(self, x, y, tile):
        """Draw tile on surface.

        Keyword arguments:
        x -- x-coordinate (tile)
        y -- y-coordinate (tile)
        tile -- Tile type
        """

        surface = pygame.display.get_surface()
        surface.blit(self.tiles[tile],
                     (x * self.tile_width,
                      y * self.tile_height))

    def draw_surface(self, x, y, tile):
        """Draw tile anywhere on surface.

        Keyword arguments:
        x -- x-coordinate (surface)
        y -- y-coordinate (surface)
        tile -- Tile type
        """

        surface = pygame.display.get_surface()
        surface.blit(self.tiles[tile], (x, y))