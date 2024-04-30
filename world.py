import pygame as pg
import os
from towers.tower_spot import TowerSpot
import pygame as pg
from enemy_data import ENEMY_SPAWN_DATA
# def draw(self, surface):
#     self.image = pg.transform.rotate(self.original_image, self.angle - 90)
#     self.rect = self.image.get_rect()
#     self.rect.center = (self.x, self.y)
#     surface.blit(self.range_image, self.range_rect)
#     surface.blit(self.image, self.rect)
class World():
    def __init__(self, data, map_image):
        self.level = 1
        self.waypoints = []
        self.level_data=data
        self.image = map_image

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
        enemies = ENEMY_SPAWN_DATA[self.level - 1]
        for enemy_type in enemies:
            enemies_to_spawn = enemies[enemy_type]





    def draw(self, surface):
        surface.blit(self.image, (0,0))
