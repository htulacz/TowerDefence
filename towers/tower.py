import pygame as pg
import consts as c
import math as m
from towers.tower_data import TOWER_DATA
class Tower(pg.sprite.Sprite):
    def __init__(self,pos,sprite_sheet):
        pg.sprite.Sprite.__init__(self)
        self.level = 0
        self.maxlevel = 3
        self.range = TOWER_DATA[self.level].get("range")
        self.cooldown = TOWER_DATA[self.level].get("cooldown")
        self.last_shot = pg.time.get_ticks()
        self.sprite_sheet = sprite_sheet
        self.animation_list = self.load_images()
        self.frame_index = 0
        self.angle = 90
        self.original_image = self.animation_list[self.frame_index]
        self.image = pg.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.update_time = pg.time.get_ticks()
        self.x = pos[0]
        self.y = pos[1]


        self.range_image = pg.Surface((self.range * 2, self.range * 2))
        self.range_image.fill('black')
        self.range_image.set_colorkey('black')
        pg.draw.circle(self.range_image, "yellow", (self.range, self.range), self.range)
        self.range_image.set_alpha(50)
        self.range_rect = self.range_image.get_rect()
        self.range_rect.center = self.rect.center

        self.target = None
        self.selected = False
    def load_images(self):
        size = self.sprite_sheet.get_height()
        animation_list = []
        for x in range(4):
            temp = self.sprite_sheet.subsurface(x * size, 0, size, size)
            animation_list.append(temp)
        return animation_list

    def update(self,enemy_group):
        if self.target:
            self.animate()
        else:
            if pg.time.get_ticks() - self.last_shot > self.cooldown:
                if not self.pick_target(enemy_group):
                    self.frame_index = 0


    def pick_target(self, enemy_group):
        x_dist = 0
        y_dist = 0
        for enemy in enemy_group:
            x_dist = enemy.pos[0] - self.x
            y_dist = enemy.pos[1] - self.y
            dist = m.sqrt(x_dist**2 + y_dist**2)
            if dist < self.range:
                self.target = enemy
                self.angle = m.degrees(m.atan2(-y_dist, x_dist))
                return True
        return False
    def animate(self):
        self.original_image = self.animation_list[self.frame_index]
        if pg.time.get_ticks() - self.update_time > c.ANIMATION_DELAY:
            self.update_time = pg.time.get_ticks()
            self.frame_index = self.frame_index + 1 if self.frame_index + 1 < 4 else 0
            self.target = None
    def upgrade(self):
        self.level += 1
        self.range = TOWER_DATA[self.level].get("range")
        self.cooldown = TOWER_DATA[self.level].get("cooldown")


        self.range_image = pg.Surface((self.range * 2, self.range * 2))
        self.range_image.fill('black')
        self.range_image.set_colorkey('black')
        pg.draw.circle(self.range_image, "yellow", (self.range, self.range), self.range)
        self.range_image.set_alpha(50)
        self.range_rect = self.range_image.get_rect()
        self.range_rect.center = self.rect.center
    def draw(self,surface):
        self.image = pg.transform.rotate(self.original_image, self.angle - 90)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        surface.blit(self.image, self.rect)
        if self.selected:
            surface.blit(self.range_image, self.range_rect)

