from towers.tower import Tower
import pygame as pg
import math as m
class Lava(Tower):
    def __init__(self, pos, time):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load("assets/towers/lava.png")
        self.rect = self.image.get_rect()
        self.pos = pos
        self.x = pos[0]
        self.y = pos[1]
        self.time = time
        self.size = 15
        self.damage = 0.1

    def shoot(self, enemy_group):
        for enemy in enemy_group:
            x_dist = self.x - enemy.pos[0]
            y_dist = self.y - enemy.pos[1]
            dist = m.sqrt(x_dist**2 + y_dist**2)
            if dist <= self.size/2:
                enemy.health -= self.damage
                if enemy.health <= 0:
                    enemy_group.remove(enemy)

    def update(self, enemy_group, bullet_group):
        if pg.time.get_ticks() - self.time > 1000:
            self.kill()
        self.shoot(enemy_group)
    def draw(self,surface):
        self.rect.center = (self.x,self.y)
        surface.blit(self.image,self.rect)