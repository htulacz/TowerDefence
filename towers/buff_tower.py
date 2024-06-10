from towers.tower import Tower
import pygame as pg
import math as m
class BuffTower(Tower):
    def __init__(self, pos, sprite_sheet, tower_group):
        super().__init__(pos, sprite_sheet)
        self.tower_group = tower_group
        for tower in tower_group:
            x_dist = tower.x - self.x
            y_dist = tower.y - self.y
            dist = m.sqrt(y_dist**2 + x_dist**2)
            if dist < self.range:
                tower.damage *= 1.25
                tower.cooldown //= 1.25
                tower.range *= 1.25

    def update(self,enemy_group):
        for tower in self.tower_group:
            x_dist = tower.x - self.x
            y_dist = tower.y - self.y
            dist = m.sqrt(y_dist**2 + x_dist**2)
            if dist < self.range:
                tower.damage *= 1.25
                tower.cooldown //= 1.25
                tower.range *= 1.25
