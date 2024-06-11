from towers.tower import Tower
import pygame as pg
import math as m
from towers.lava import Lava
class LavaTower(Tower):
    def __init__(self, pos, sprite_sheet, tower_group):
        super().__init__(pos, sprite_sheet)
        self.lava_time = 10




    def shoot(self,enemy_group):
        lava = Lava()