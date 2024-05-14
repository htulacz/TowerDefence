import pygame as pg
import os
from towers.tower_spot import TowerSpot
import pygame as pg
from enemy_data import ENEMY_SPAWN_DATA
import random
import consts as c

# def draw(self, surface):
#     self.image = pg.transform.rotate(self.original_image, self.angle - 90)
#     self.rect = self.image.get_rect()
#     self.rect.center = (self.x, self.y)
#     surface.blit(self.range_image, self.range_rect)
#     surface.blit(self.image, self.rect)
class World():
    spawned_enemies: int

    def __init__(self, data, map_images={}):
        pg.sprite.Sprite.__init__(self)
        """
        @type map_images: object
        """
        self.health = c.HEALTH
        self.money = c.MONEY
        self.level = 1
        self.tile_map = []
        self.waypoints = []
        self.level_data=data
        self.angle = 0
        self.orginal_image = map_images.get(str(self.level))
        self.image = pg.transform.rotate(self.orginal_image, self.angle)
        self.enemy_list = []
        self.spawned_enemies = 0

    def process_data(self):

        for layer in self.level_data["layers"]:
            if layer["name"] == "waypoints":
                for obj in layer["objects"]:
                    waypoint_data=obj["polyline"]
                    for point in waypoint_data:
                        temp_x=point.get("x")+obj["x"]
                        temp_y=point.get("y")+obj["y"]
                        self.waypoints.append((temp_x,temp_y))

    def process_enemies(self):
        print(self.level)
        enemies = ENEMY_SPAWN_DATA[self.level - 1]
        for enemy_type in enemies:
            enemies_to_spawn = enemies[enemy_type]
            for enemy in range(enemies_to_spawn):
                self.enemy_list.append(enemy_type)
        random.shuffle(self.enemy_list)


    def draw(self, surface):
        surface.blit(self.image, (0,0))
