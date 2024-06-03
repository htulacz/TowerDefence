import pygame as pg
from pygame.math import Vector2
import math


from enemy_data import ENEMY_DATA
import consts as c

class Enemy(pg.sprite.Sprite):
    def __init__(self,enemy_type, waypoints, images, images_features):
        #ZOBACZĆ CZEMU NIE DZIAŁA SUPER()

        pg.sprite.Sprite.__init__(self)
        self.speed = 2
        self.waypoints = waypoints
        self.pos = Vector2(self.waypoints[0])
        self.target_waypoint = 1
        self.max_health=ENEMY_DATA.get(enemy_type)["health"]
        self.health = ENEMY_DATA.get(enemy_type)["health"]
        self.speed = ENEMY_DATA.get(enemy_type)["speed"]
        self.angle = 0
        self.original_image = images.get(enemy_type)
        self.image = pg.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.reached_goal = False
        self.image_feature = images_features.get(enemy_type)
        self.shield = True
        self.enemy_type = enemy_type
        self.fire=False
        self.last_health=self.health
        self.is_shadow = False


    def update(self, world):
        self.move(world)
        self.rotate()
        self.check_alive(world)


    def move(self, world):
        # define a target waypoint
        if self.target_waypoint < len(self.waypoints):
            self.target = Vector2(self.waypoints[self.target_waypoint])
            self.movement = self.target - self.pos
        else:
            # enemy has reached the end of the path
            self.reached_goal = True
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

    def feature(self):
        match self.enemy_type:
            case "weak":
                self.weak_function()
                print("plonie do konca i obrazenia ma x2")
            case "medium":
                print("You chose a banana.")
            case "strong":
                self.strong_function()
                print("ma shield na poczatku")
            case "elite":
                print("Sorry, that fruit is not available.")
            case "super":
                print("super")
            case "boss" :
                print("boss")
    def strong_function(self):
        if self.shield:
            if self.health < self.max_health:
                self.health=self.max_health
                self.shield =False
                self.original_image =self.original_image
                self.image=self.original_image
            else:
                self.original_image =pg.image.load("assets/enemies/e3_shield.png").convert_alpha()
                self.health=self.health-1
        else:
            self.original_image = pg.image.load("assets/enemies/e3_shield.png").convert_alpha()

        # Obróć obrazek i zaktualizuj prostokąt
        self.image = pg.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=self.pos)

    def weak_function(self):
        if self.health != self.max_health:
            self.health=self.health-(self.last_health-self.health)
            self.last_health=self.health
            self.image= pg.image.load("assets/enemies/e1_fire.png").convert_alpha()


