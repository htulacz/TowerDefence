import pygame as pg
from pygame.math import Vector2
import math
from enemy_data import ENEMY_DATA

class Enemy(pg.sprite.Sprite):
<<<<<<<<< Temporary merge branch 1
    def __init__(self, enemy_type, waypoints, images):
=========
    def __init__(self, waypoints, image):
        #ZOBACZĆ CZEMU NIE DZIAŁA SUPER()
>>>>>>>>> Temporary merge branch 2
        pg.sprite.Sprite.__init__(self)
        self.speed = 2
        self.hp = 10
        self.waypoints = waypoints
        self.pos = Vector2(self.waypoints[0])
        self.target_waypoint = 1
        self.health = ENEMY_DATA.get(enemy_type)["health"]
        self.speed = ENEMY_DATA.get(enemy_type)["speed"]
        self.angle = 0
        self.original_image = images.get(enemy_type)
        self.image = pg.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def move(self):
        if self.target_waypoint < len(self.waypoints):
            self.target = Vector2(self.waypoints[self.target_waypoint])
            self.movement = self.target - self.pos
        else:
            self.kill()

        dist = self.movement.length()
        if dist < self.speed:
            if dist != 0:
                self.pos += self.movement.normalize() * dist
            self.target_waypoint += 1
        else:
            self.pos += self.movement.normalize() * self.speed

        self.rect.center = self.pos

    def update(self):
        self.move()