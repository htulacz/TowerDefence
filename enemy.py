import pygame as pg
from pygame.math import Vector2
import math
from enemy_data import ENEMY_DATA
import consts as c

class Enemy(pg.sprite.Sprite):
    def __init__(self,enemy_type, waypoints, images):
        #ZOBACZĆ CZEMU NIE DZIAŁA SUPER()
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

    def update(self, world):
        self.move(world)
        self.rotate()
        self.check_alive(world)
    # def move(self):
    #     if self.target_waypoint < len(self.waypoints):
    #         self.target = Vector2(self.waypoints[self.target_waypoint])
    #         self.movement = self.target - self.pos
    #     else:
    #         self.kill()
    #
    #     dist = self.movement.length()
    #     if dist < self.speed:
    #         if dist != 0:
    #             self.pos += self.movement.normalize() * dist
    #         self.target_waypoint += 1
    #     else:
    #         self.pos += self.movement.normalize() * self.speed
    #
    #     self.rect.center = self.pos

    # def update(self):
    #     self.move()

    def move(self, world):
        # define a target waypoint
        if self.target_waypoint < len(self.waypoints):
            self.target = Vector2(self.waypoints[self.target_waypoint])
            self.movement = self.target - self.pos
        else:
            # enemy has reached the end of the path
            self.kill()
            world.health -= 1

        # calculate distance to target
        dist = self.movement.length()
        # check if remaining distance is greater than the enemy speed
        if dist >= self.speed:
            self.pos += self.movement.normalize() * self.speed
        else:
            if dist != 0:
                self.pos += self.movement.normalize() * dist
            self.target_waypoint += 1

    def rotate(self):
        # calculate distance to next waypoint
        dist = self.target - self.pos
        # use distance to calculate angle
        self.angle = math.degrees(math.atan2(-dist[1], dist[0]))
        # rotate image and update rectangle
        self.image = pg.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def check_alive(self, world):
        if self.health <= 0:
            world.money += c.KILL_REWARD
            self.kill()