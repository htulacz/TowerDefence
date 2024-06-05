from towers.tower import Tower
import pygame as pg
import math as m
class BombTower(Tower):
    def __init__(self, pos, sprite_sheet):
        super().__init__(pos, sprite_sheet)
        self.explosion_radii = 10
        self.targets = []

    def pick_target(self, enemy_group):
        x_dist = 0
        y_dist = 0
        targets = []
        for enemy in enemy_group:
            x_dist = enemy.pos[0] - self.x
            y_dist = enemy.pos[1] - self.y
            dist = m.sqrt(x_dist ** 2 + y_dist ** 2)
            if dist < self.range:
                self.target = enemy
                self.angle = m.degrees(m.atan2(-y_dist, x_dist))
                break
        if self.target:
            for enemy in enemy_group:
                x_dist = enemy.pos[0] - self.x
                y_dist = enemy.pos[1] - self.y
                dist = m.sqrt(x_dist ** 2 + y_dist ** 2)
                if dist < self.range:
                    targets.append(enemy)

            self.targets = targets
    def shoot(self,enemy_group):
        for target in self.targets:
            target.health -= self.damage
            if target.health <= 0:
                enemy_group.remove(target)