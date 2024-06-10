from towers.tower import Tower
import pygame as pg
import math as m
class Lava(Tower):
    def __init__(self, pos, sprite_sheet, time):
        super().__init__(pos, sprite_sheet)
        self.time = time
        self.size = 10

    def shoot(self, enemy_group):
        for enemy in enemy_group:
            x_dist = self.x - enemy.pos[0]
            y_dist = self.y - enemy.pos[1]
            dist = m.sqrt(x_dist**2 + y_dist**2)
            if dist <= 10:
                enemy.health -= self.damage
                if enemy.health <= 0:
                    enemy_group.remove(enemy)
