from towers.tower import Tower
import pygame as pg
import math as m
class BuffTower(Tower):
    def __init__(self, pos, sprite_sheet, tower_group):
        super().__init__(pos, sprite_sheet)
        self.tower_group = tower_group
        self.range *= 2
        self.range_image = pg.Surface((self.range * 4, self.range * 4))
        self.range_image.fill('black')
        self.range_image.set_colorkey('black')
        pg.draw.circle(self.range_image, "yellow", (self.x, self.y), self.range)
        self.range_image.set_alpha(50)
        self.range_rect = self.range_image.get_rect()
        for tower in tower_group:
            x_dist = tower.x - self.x
            y_dist = tower.y - self.y
            dist = m.sqrt(y_dist**2 + x_dist**2)
            if dist < self.range and not tower.buffed:
                tower.damage *= 1.25
                tower.cooldown //= 1.25
                tower.range *= 1.25
                tower.buffed = True

    def update(self, enemy_group, bullet_group):
        for tower in self.tower_group:
            x_dist = tower.x - self.x
            y_dist = tower.y - self.y
            dist = m.sqrt(y_dist**2 + x_dist**2)
            if dist < self.range and not tower.buffed:
                tower.damage *= 1.25
                tower.cooldown //= 1.25
                tower.range *= 1.25
                tower.buffed = True

    def upgrade(self):
        super().upgrade()
        self.range *= 2
        self.range_image = pg.Surface((self.range * 4, self.range * 4))
        self.range_image.fill('black')
        self.range_image.set_colorkey('black')
        pg.draw.circle(self.range_image, "yellow", (self.x, self.y), self.range)
        self.range_image.set_alpha(50)
        self.range_rect = self.range_image.get_rect()