import pygame as pg
import consts as c
import math as m
from towers.tower_data import TOWER_DATA
from pygame.math import Vector2
class Bullet(pg.sprite.Sprite):
    def __init__(self,pos,dest):
        pg.sprite.Sprite.__init__(self)
        self.pos = Vector2(pos[0],pos[1])
        self.dest = Vector2(dest[0],dest[1])
        self.image = pg.image.load("assets/towers/bullet.png")
        self.speed = 10
        self.rect = self.image.get_rect()

    def move(self):
        if self.pos == self.dest:
            self.kill()
        movement = self.dest - self.pos
        distance = movement.length()
        if distance >= self.speed:
            self.pos += movement.normalize() * self.speed
        else:
            if distance != 0:
                self.pos += movement.normalize() * distance


    def update(self):
        self.move()
        self.rect.center = self.pos

    def draw(self,surface):
        surface.blit(self.image, self.rect)
