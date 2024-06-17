from towers.tower import Tower
import pygame as pg
import math as m
class BombTower(Tower):
    def __init__(self, pos, sprite_sheet):
        super().__init__(pos, sprite_sheet)
        self.explosion_radii = 10
        self.range //= 2
        self.cooldown *= 2



    def shoot(self,enemy_group):
        self.target.health -= self.damage
        if self.target.health <= 0:
            enemy_group.remove(self.target)
        for enemy in enemy_group:
            x_dist = enemy.pos[0] - self.target.pos[0]
            y_dist = enemy.pos[1] - self.target.pos[1]
            dist = m.sqrt(x_dist**2 + y_dist**2)
            if dist < self.explosion_radii:
                enemy.health -= self.damage
                if enemy.health <= 0:
                    enemy_group.remove(enemy)