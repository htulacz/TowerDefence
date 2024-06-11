from towers.tower import Tower
import pygame as pg
class IceTower(Tower):
    def __init__(self, pos, sprite_sheet):
        super().__init__(pos, sprite_sheet)
        self.slow_effect = 0.9

    def shoot(self,enemy_group):
        self.target.health -= self.damage
        self.target.speed *= self.slow_effect
        if self.target.health <= 0:
            enemy_group.remove(self.target)