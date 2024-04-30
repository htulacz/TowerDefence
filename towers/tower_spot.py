import pygame as pg
class TowerSpot(pg.sprite.Sprite):
    def __init__(self, pos, image):
        pg.sprite.Sprite.__init__(self)
        self.x = pos[0]
        self.y = pos[1]
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.radii = self.rect.width / 2
        self.occupied = False


    def draw(self,surface):
        surface.blit(self.image, self.rect)
