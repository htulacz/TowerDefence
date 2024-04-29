import json
import os
import _json
import pygame as pg
import consts as c
from enemy import Enemy
from world import World
from button import Button
from towers.tower import Tower


pg.init()
clock = pg.time.Clock()


screen = pg.display.set_mode((c.SCREEN_WIDTH + c.SIDE_PANEL,c.SCREEN_HEIGTH))
pg.display.set_caption("Tower Defense")
run = True

last_enemy_spawn = pg.time.get_ticks()

tower_sheet = pg.image.load("toweranimation.png").convert_alpha()
tower_image = pg.image.load("t1.png").convert_alpha()
enemy_image = pg.image.load("assets/enemies/e3.png").convert_alpha()
tower_button_img = pg.image.load("towerbutton.png").convert_alpha()
cancel_button_img = pg.image.load("cancelbutton.png").convert_alpha()
map_image = pg.image.load("assets/maps/map1.png").convert_alpha()
enemies_images={
    "weak": pg.image.load("assets/enemies/e1.png").convert_alpha(),
    "medium": pg.image.load("assets/enemies/e2.jpg").convert_alpha(),
    "strong": pg.image.load("assets/enemies/e3.png").convert_alpha(),
    "elite": pg.image.load("assets/enemies/e4.png").convert_alpha()
}



with open('assets/points/points1.tmj') as file:
    world_data = json.load(file)

world = World(world_data,map_image);
world.process_data()
world.process_enemies()

placing_towers = False
selected_towers = None


enemy_group = pg.sprite.Group()
tower_group = pg.sprite.Group()

#enemy_type="weak"
#enemy = Enemy(enemy_type,world.waypoints,enemies_images)
#enemy_group.add(enemy)


tower_button = Button(c.SCREEN_WIDTH + 30, 120, tower_button_img)
cancel_button = Button(c.SCREEN_WIDTH + 160, 120, cancel_button_img)
# map.draw(screen)
def create_tower(click_pos):
    tower = Tower(click_pos, tower_sheet)
    tower_group.add(tower)



while run:
    clock.tick(c.FPS)

    screen.fill("grey100")
    world.draw(screen)

    enemy_group.update()
    for tower in tower_group:
        tower.draw(screen)

    enemy_group.draw(screen)
    tower_group.update(enemy_group)

    #spawn enemies
    if pg.time.get_ticks() - last_enemy_spawn > c.SPAWN_COOLDOWN:
        # skonczylam 11;40
        if world.spawned_enemies < len(world.enemy_list):
            enemy_type=world.enemy_list[world.spawned_enemies]
            enemy = Enemy(enemy_type,world.waypoints,enemies_images)
            enemy_group.add(enemy)
            world.spawned_enemies+=1
            last_enemy_spawn=pg.time.get_ticks()

    if tower_button.draw(screen):
        placing_towers = True
    if placing_towers:
        hover_rect = tower_image.get_rect()
        hover_pos = pg.mouse.get_pos()
        hover_rect.center = hover_pos
        if hover_pos[0] <= c.SCREEN_WIDTH:
            screen.blit(tower_image, hover_rect)
        if cancel_button.draw(screen):
            placing_towers = False

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            click_pos = pg.mouse.get_pos()
            if click_pos[0] < c.SCREEN_WIDTH and click_pos[1] < c.SCREEN_HEIGTH:
                if placing_towers:
                    create_tower(click_pos)

    pg.display.flip()


pg.quit()
