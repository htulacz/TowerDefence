import pygame as pg
import json
from enemy import Enemy
from world import World
from button import Button
import consts as c
from runner import play

from towers.tower import Tower
from towers.tower_spot import TowerSpot
pg.init()
clock = pg.time.Clock()


screen = pg.display.set_mode((c.SCREEN_WIDTH + c.SIDE_PANEL,c.SCREEN_HEIGTH))
pg.display.set_caption("Tower Defense")
run = True

tower_sheet = pg.image.load("toweranimation.png").convert_alpha()
tower_image = pg.image.load("t1.png").convert_alpha()
#enemy_image = pg.image.load("assets/enemies/e3.png").convert_alpha()
tower_button_img = pg.image.load("towerbutton.png").convert_alpha()
cancel_button_img = pg.image.load("cancelbutton.png").convert_alpha()
map_image = pg.image.load("assets/maps/map1.png").convert_alpha()
tower_spot_image = pg.image.load("assets/towerspot.png").convert_alpha()
enemies_images={
    "weak": pg.image.load("assets/enemies/e1.png").convert_alpha(),
    "medium": pg.image.load("assets/enemies/e2.jpg").convert_alpha(),
    "strong": pg.image.load("assets/enemies/e3.png").convert_alpha(),
    "elite": pg.image.load("assets/enemies/e4.png").convert_alpha()
}



with open('assets/points/points1.tmj') as file:
    world_data = json.load(file)

world = World(world_data,map_image)
world.process_data()
world.process_enemies()

last_enemy_spawn = pg.time.get_ticks()
placing_towers = False
selected_towers = None


start_image = pg.image.load("assets/menustart.png")
leaderboard_image = pg.image.load("assets/menuleaderboard.png")
exit_image = pg.image.load("assets/menuexit.png")
enemy_group = pg.sprite.Group()
tower_group = pg.sprite.Group()
spots_group = pg.sprite.Group()


start_button = Button(c.SCREEN_WIDTH//2, c.SCREEN_HEIGTH//3 - 150, start_image)
leaderboard_button = Button(c.SCREEN_WIDTH//2, c.SCREEN_HEIGTH//3 * 2 - 150, leaderboard_image)
exit_button = Button(c.SCREEN_WIDTH//2, c.SCREEN_HEIGTH - 150, exit_image)



tower_spots = [(92,230)]
for spot in tower_spots:
    spots_group.add(TowerSpot(spot, tower_spot_image))

tower_button = Button(c.SCREEN_WIDTH + 30, 120, tower_button_img)
cancel_button = Button(c.SCREEN_WIDTH + 160, 120, cancel_button_img)
# map.draw(screen)
def create_tower(click_pos):
    tower = Tower(click_pos, tower_sheet)
    tower_group.add(tower)

def check_for_spot(click_pos):
    for spot in spots_group:
        if (click_pos[0] - spot.x)**2 + (click_pos[1] - spot.y)**2 <= spot.radii**2:
            return spot.rect.center
    return False


while run:

    clock.tick(c.FPS)

    screen.fill("grey100")
    world.draw(screen)
    spots_group.draw(screen)
    enemy_group.update(world)


    for tower in tower_group:
        tower.draw(screen)
    if pg.time.get_ticks() - last_enemy_spawn > c.SPAWN_COOLDOWN:
        if world.spawned_enemies < len(world.enemy_list):
            enemy_type = world.enemy_list[world.spawned_enemies]
            enemy = Enemy(enemy_type, world.waypoints, enemies_images)
            enemy_group.add(enemy)
            world.spawned_enemies +=1
            last_enemy_spawn=pg.time.get_ticks()

    if start_button.draw(screen):
        play()
    if leaderboard_button.draw(screen):
        print("todo")
    if exit_button.draw(screen):
        run = False

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            click_pos = pg.mouse.get_pos()
            if click_pos[0] < c.SCREEN_WIDTH and click_pos[1] < c.SCREEN_HEIGTH:
                actual_place = check_for_spot(click_pos)
                if placing_towers and actual_place:
                    create_tower(actual_place)

    pg.display.flip()
pg.quit()
