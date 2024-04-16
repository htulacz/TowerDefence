import pygame as pg
import os


# def draw(self, surface):
#     self.image = pg.transform.rotate(self.original_image, self.angle - 90)
#     self.rect = self.image.get_rect()
#     self.rect.center = (self.x, self.y)
#     surface.blit(self.range_image, self.range_rect)
#     surface.blit(self.image, self.rect)
class Map:
    def __init__(self, map_image):
        self.image = map_image

    def draw(self, surface):
        surface.blit(self.image, (0,0))
