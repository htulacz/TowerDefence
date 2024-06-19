from towers.tower import Tower
import pygame as pg
import math as m
class BombTower(Tower):
    def __init__(self, pos, sprite_sheet, screen):
        super().__init__(pos, sprite_sheet)
        self.explosion_radii = 50
        self.cooldown *= 2
        self.explosion_image = pg.Surface((self.explosion_radii * 2, self.explosion_radii * 2))
        self.exp_rect = self.explosion_image.get_rect()
        self.explosion_image.fill('black')
        self.explosion_image.set_colorkey('black')
        self.screen = screen

    def shoot(self, enemy_group):
        self.target.health -= self.damage
        if self.target.health <= 0:
            enemy_group.remove(self.target)

        self.explosion_image.fill('black')

        explosion_center = (self.target.pos[0], self.target.pos[1])
        pg.draw.circle(self.explosion_image, 'red', (self.explosion_radii, self.explosion_radii), self.explosion_radii)

        self.exp_rect.center = explosion_center
        self.screen.blit(self.explosion_image, self.exp_rect)

        for enemy in enemy_group:
            x_dist = enemy.pos[0] - self.target.pos[0]
            y_dist = enemy.pos[1] - self.target.pos[1]
            dist = m.sqrt(x_dist ** 2 + y_dist ** 2)

            if dist < self.explosion_radii:
                enemy.health -= self.damage
                if enemy.health <= 0:
                    enemy_group.remove(enemy)

    def upgrade(self):
        super().upgrade()
        self.cooldown *= 2