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
# enemies_images={
#     "weak": pg.image.load("assets/enemies/e1.png").convert_alpha(),
#     "medium": pg.image.load("assets/enemies/e2.jpg").convert_alpha(),
#     "strong": pg.image.load("assets/enemies/e3.png").convert_alpha(),
#     "elite": pg.image.load("assets/enemies/e4.png").convert_alpha()
# }
#
#
# map_images={
#         "1" : pg.image.load("assets/maps/map2.jpeg").convert_alpha(),
#         "2" : pg.image.load("assets/maps/map2.jpeg").convert_alpha(),
#         "3" : pg.image.load("assets/maps/map3.jpg").convert_alpha(),
#         "4" : pg.image.load("assets/maps/map4.jpg").convert_alpha(),
#         "5" : pg.image.load("assets/maps/map5.png").convert_alpha(),
#         "6" : pg.image.load("assets/maps/map6.png").convert_alpha(),
#         "7" : pg.image.load("assets/maps/map7.png").convert_alpha(),
#         "8" : pg.image.load("assets/maps/map8.png").convert_alpha()
#     }
# with open('assets/points/points1.tmj') as file:
#     world_data = json.load(file)

# world = World(world_data,map_images)
# world.process_data()
# world.process_enemies()
level_started=False
#last_enemy_spawn = pg.time.get_ticks()
placing_towers = False
selected_towers = None


start_image = pg.image.load("assets/menustart.png")
leaderboard_image = pg.image.load("assets/menuleaderboard.png")
exit_image = pg.image.load("assets/menuexit.png")
leave_image = pg.image.load("assets/menuleave.png")
start_button = Button(c.SCREEN_WIDTH//2, c.SCREEN_HEIGTH//3 - 150, start_image)
leaderboard_button = Button(c.SCREEN_WIDTH//2, c.SCREEN_HEIGTH//3 * 2 - 150, leaderboard_image)
exit_button = Button(c.SCREEN_WIDTH//2, c.SCREEN_HEIGTH - 150, exit_image)
leave_button = Button(0, 0, leave_image)

leaderboard_is_open = False
scoreboard_surface = None
level=1
while run:
    # world = World(world_data, map_images)
    # world.level=level
    # world.process_data()
    # world.process_enemies()
    clock.tick(c.FPS)
    screen.fill("grey100")
    if not leaderboard_is_open and start_button.draw(screen):
        ############################################################
        play()
    if not leaderboard_is_open and leaderboard_button.draw(screen):
        leaderboard_is_open = True
        with open("scores/scores.json", "r") as file:
            scoreboard = json.load(file)
        scoreboard_surface = pg.Surface((c.SCREEN_WIDTH, c.SCREEN_HEIGTH))
        scoreboard_surface.fill((255, 255, 255))
        font = pg.font.Font(None, 36)
        y = 50
        for s in scoreboard:
            text = font.render(str(s), True, (0,0,0))
            text_rect = text.get_rect()
            text_rect.center = (c.SCREEN_WIDTH // 2, y)
            y += 40
            scoreboard_surface.blit(text, text_rect)
    if not leaderboard_is_open and exit_button.draw(screen):
        run = False

    if leaderboard_is_open:
        if leave_button.draw(scoreboard_surface):
            leaderboard_is_open = False
        screen.blit(scoreboard_surface, (0, 0))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    pg.display.flip()

pg.quit()
