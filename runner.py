
# import json
# import pygame as pg
# import consts as c
# from world import World
# from enemy import Enemy
# from world import World
# from button import Button
# # from towers.archer_tower import ArcherTower
# # from towers.bomb_tower import BombTower
# from towers.tower import Tower
# from towers.tower_spot import TowerSpot
#
#
# def play():
#     pg.init()
#     clock = pg.time.Clock()
#     run = True
#     screen = pg.display.set_mode((c.SCREEN_WIDTH + c.SIDE_PANEL, c.SCREEN_HEIGTH))
#     pg.display.set_caption("Tower Defense")
#     ###########
#     tower_sheet = pg.image.load("toweranimation.png").convert_alpha()
#     tower_image = pg.image.load("t1.png").convert_alpha()
#     # enemy_image = pg.image.load("assets/enemies/e3.png").convert_alpha()
#     tower_button_img = pg.image.load("towerbutton.png").convert_alpha()
#     cancel_button_img = pg.image.load("cancelbutton.png").convert_alpha()
#     upgrade_button_img = pg.image.load("upgradebutton.png").convert_alpha()
#     # map_image = pg.image.load("assets/maps/map1.png").convert_alpha()
#     tower_spot_image = pg.image.load("assets/towerspot.png").convert_alpha()
#
#     map_images = {
#         "1": pg.image.load("assets/maps/map1.png").convert_alpha(),
#         "2": pg.image.load("assets/maps/map2.png").convert_alpha(),
#         "3": pg.image.load("assets/maps/map3.png").convert_alpha(),
#         "4": pg.image.load("assets/maps/map4.png").convert_alpha(),
#         # "5": pg.image.load("assets/maps/map5.png").convert_alpha(),
#         # "6": pg.image.load("assets/maps/map6.png").convert_alpha(),
#         # "7": pg.image.load("assets/maps/map7.png").convert_alpha(),
#         # "8": pg.image.load("assets/maps/map8.png").convert_alpha()
#     }
#
#     enemy_images = {
#         "weak": pg.image.load("assets/enemies/e1.png").convert_alpha(),
#         "medium": pg.image.load("assets/enemies/e2.png").convert_alpha(),
#         "strong": pg.image.load("assets/enemies/e3.png").convert_alpha(),
#         "elite": pg.image.load("assets/enemies/e4.png").convert_alpha(),
#         "super": pg.image.load("assets/enemies/e3.png").convert_alpha(),
#         "boss": pg.image.load("assets/enemies/e4.png").convert_alpha()
#     }
#
#     with open('assets/points/points1.tmj') as file:
#         world_data = json.load(file)
#
#     world: World = World(world_data, map_images)
#     world.process_data()
#     world.process_enemies()
#     text_font = pg.font.SysFont("Consolas", 15, bold=True)
#     large_font = pg.font.SysFont("Consolas", 36)
#
#     def draw_text(text, font, text_col, x, y):
#         img = font.render(text, True, text_col)
#         screen.blit(img, (x, y))
#
#     def draw_next_button_text(button, text, font, color):
#         text_img = font.render(text, True, color)
#         text_rect = text_img.get_rect(
#             center=(button.rect.x + button.rect.width // 2, button.rect.y + button.rect.height // 2))
#         screen.blit(text_img, text_rect)
#
#     placing_towers = False
#     selected_tower = None
#
#     enemy_group = pg.sprite.Group()
#     tower_group = pg.sprite.Group()
#     spots_group = pg.sprite.Group()
#
#     with open("assets/towerspots/spots1.json") as file:
#         tower_spots = json.load(file)
#     for spot in tower_spots:
#         spots_group.add(TowerSpot(spot, tower_spot_image))
#
#     tower_button = Button(c.SCREEN_WIDTH + 30, 120, tower_button_img)
#     cancel_button = Button(c.SCREEN_WIDTH + 160, 120, cancel_button_img)
#     upgrade_button = Button(c.SCREEN_WIDTH + 30, 160, upgrade_button_img)
#     next_level_button = Button(c.SCREEN_WIDTH + 30, 200, tower_button_img)  # **Nowy przycisk**
#
#     def create_tower(click_pos):
#         tower = Tower(click_pos, tower_sheet)
#         tower_group.add(tower)
#
#     def check_for_spot(click_pos):
#         for spot in spots_group:
#             if not spot.occupied:
#                 if (click_pos[0] - spot.x) ** 2 + (click_pos[1] - spot.y) ** 2 <= spot.radii ** 2:
#                     spot.occupied = True
#                     return spot.rect.center
#         return False
#
#     def select_tower(click_pos):
#         x = click_pos[0]
#         y = click_pos[1]
#         for tower in tower_group:
#             c = tower.rect.center
#             width = tower.rect.width
#             if x > c[0] - width and x < c[0] + width and y > c[1] - width and y < c[1] + width:
#                 tower.selected = True
#                 return tower
#
#     def clear_selection():
#         for tower in tower_group:
#             tower.selected = False
#
#     def runner():
#         nonlocal run
#         nonlocal placing_towers
#         nonlocal selected_tower
#         last_enemy_spawn = pg.time.get_ticks()
#         score = 0
#         next_level_ready = False  # **Flaga gotowości do następnego poziomu**
#
#         while run:
#             score += 1
#             clock.tick(c.FPS)
#             screen.fill("grey100")
#             world.draw(screen)
#             enemy_group.draw(screen)
#             spots_group.draw(screen)
#             enemy_group.update(world)
#             tower_group.update(enemy_group)
#             for tower in tower_group:
#                 tower.draw(screen)
#             draw_text("health:", text_font, "grey100", 0, 0)
#             draw_text(str(world.health), text_font, "grey100", 0, 30)
#             draw_text("money:", text_font, "grey100", 0, 60)
#             draw_text("level:", text_font, "grey100", 0, 120)
#             draw_text(str(world.level), text_font, "grey100", 0, 150)
#
#             if not next_level_ready:
#                 if pg.time.get_ticks() - last_enemy_spawn > c.SPAWN_COOLDOWN:
#                     if world.spawned_enemies < len(world.enemy_list):
#                         enemy_type = world.enemy_list[world.spawned_enemies]
#                         enemy = Enemy(enemy_type, world.waypoints, enemy_images)
#                         enemy_group.add(enemy)
#                         world.spawned_enemies += 1
#                         last_enemy_spawn = pg.time.get_ticks()
#
#                 # **Sprawdź, czy wszyscy wrogowie dotarli do ostatniego punktu**
#                 all_enemies_reached = all(enemy.reached_goal for enemy in enemy_group)
#                 if world.spawned_enemies == len(world.enemy_list) and all_enemies_reached:
#                     next_level_ready = True
#
#             if next_level_ready:
#                 draw_text("Next Level Available", large_font, "red", c.SCREEN_WIDTH // 2, c.SCREEN_HEIGTH // 2)
#                 if next_level_button.draw(screen):
#                     next_level_ready = False
#                     world.level += 1
#                     world.enemy_list = []
#                     with open(f"assets/points/points{world.level}.tmj") as file:
#                         world_data = json.load(file)
#                         print("2")
#                     world.level_data = world_data
#                     world.waypoints = []
#                     world.process_data()
#                     world.process_enemies()
#                     print(world.waypoints)
#                     world.original_image = map_images.get(str(world.level))
#                     world.image = pg.transform.rotate(world.original_image, world.angle)
#                     world.spawned_enemies = 0
#                 draw_next_button_text(next_level_button, "Next Level", text_font, "black")
#
#             if tower_button.draw(screen):
#                 placing_towers = True
#             if placing_towers:
#                 hover_rect = tower_image.get_rect()
#                 hover_pos = pg.mouse.get_pos()
#                 hover_rect.center = hover_pos
#                 if hover_pos[0] <= c.SCREEN_WIDTH:
#                     screen.blit(tower_image, hover_rect)
#                 if cancel_button.draw(screen):
#                     placing_towers = False
#             if selected_tower and selected_tower.level < selected_tower.maxlevel:
#                 if upgrade_button.draw(screen):
#                     selected_tower.upgrade()
#
#             for event in pg.event.get():
#                 if event.type == pg.QUIT:
#                     run = False
#                 if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
#                     click_pos = pg.mouse.get_pos()
#                     if click_pos[0] < c.SCREEN_WIDTH and click_pos[1] < c.SCREEN_HEIGTH:
#                         actual_place = check_for_spot(click_pos)
#                         selected_tower = None
#                         clear_selection()
#                         if placing_towers and actual_place:
#                             create_tower(actual_place)
#                         else:
#                             selected_tower = select_tower(click_pos)
#
#             pg.display.flip()
#         with open("scores/scores.json", "r") as file:
#             existing_scores = json.load(file)
#         existing_scores.append(score)
#         existing_scores.sort(reverse=True)
#         with open("scores/scores.json", "w") as file:
#             json.dump(existing_scores, file)
#
#     runner()

import json
import pygame as pg
import consts as c
from world import World
from enemy import Enemy
from button import Button
from towers.archer_tower import ArcherTower
# from towers.bomb_tower import BombTower
from towers.tower import Tower
from towers.tower_spot import TowerSpot

def play():
    pg.init()
    clock = pg.time.Clock()
    run = True
    screen = pg.display.set_mode((c.SCREEN_WIDTH + c.SIDE_PANEL, c.SCREEN_HEIGTH))
    pg.display.set_caption("Tower Defense")

    tower_sheet = pg.image.load("toweranimation.png").convert_alpha()
    tower_image = pg.image.load("assets/towers/tower1.png").convert_alpha()
    tower_button_img = pg.image.load("towerbutton.png").convert_alpha()
    cancel_button_img = pg.image.load("cancelbutton.png").convert_alpha()
    upgrade_button_img = pg.image.load("upgradebutton.png").convert_alpha()
    tower_spot_image = pg.image.load("assets/towerspot.png").convert_alpha()
    next_lvl_image= pg.image.load("upgradebutton.png").convert_alpha()


    map_images = {
        "1": pg.image.load("assets/maps/map1.png").convert_alpha(),
        "2": pg.image.load("assets/maps/map2.png").convert_alpha(),
        "3": pg.image.load("assets/maps/map3.png").convert_alpha(),
        "4": pg.image.load("assets/maps/map4.png").convert_alpha(),
    }

    enemy_images = {
        "weak": pg.image.load("assets/enemies/e1.png").convert_alpha(),
        "medium": pg.image.load("assets/enemies/e2.png").convert_alpha(),
        "strong": pg.image.load("assets/enemies/e3.png").convert_alpha(),
        "elite": pg.image.load("assets/enemies/e4.png").convert_alpha(),
        "super": pg.image.load("assets/enemies/e5.png").convert_alpha(),
        "boss": pg.image.load("assets/enemies/e6.png").convert_alpha()
    }

    with open('assets/points/points1.tmj') as file:
        world_data = json.load(file)

    world: World = World(world_data, map_images)
    world.process_data()
    world.process_enemies()
    text_font = pg.font.SysFont("Consolas", 15, bold=True)
    large_font = pg.font.SysFont("Consolas", 36)

    def draw_text(text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        screen.blit(img, (x, y))

    def draw_next_button_text(button, text, font, color):
        text_img = font.render(text, True, color)
        text_rect = text_img.get_rect(
            center=(button.rect.x + button.rect.width // 2, button.rect.y + button.rect.height // 2))
        screen.blit(text_img, text_rect)

    placing_towers = False
    selected_tower = None

    enemy_group = pg.sprite.Group()
    tower_group = pg.sprite.Group()
    spots_group = pg.sprite.Group()

    with open("assets/towerspots/spots1.json") as file:
        tower_spots = json.load(file)
    for spot in tower_spots:
        spots_group.add(TowerSpot(spot, tower_spot_image))

    tower_button = Button(c.SCREEN_WIDTH + 30, 120, tower_button_img)
    cancel_button = Button(c.SCREEN_WIDTH + 160, 120, cancel_button_img)
    upgrade_button = Button(c.SCREEN_WIDTH + 30, 160, upgrade_button_img)
    next_level_button = Button(c.SCREEN_WIDTH + 30, 200, next_lvl_image)  # **Nowy przycisk**

    def create_tower(click_pos):
        tower = ArcherTower(click_pos, tower_sheet)
        tower_group.add(tower)

    def check_for_spot(click_pos):
        for spot in spots_group:
            if not spot.occupied:
                if (click_pos[0] - spot.x) ** 2 + (click_pos[1] - spot.y) ** 2 <= spot.radii ** 2:
                    spot.occupied = True
                    return spot.rect.center
        return False

    def select_tower(click_pos):
        x = click_pos[0]
        y = click_pos[1]
        for tower in tower_group:
            c = tower.rect.center
            width = tower.rect.width
            if x > c[0] - width and x < c[0] + width and y > c[1] - width and y < c[1] + width:
                tower.selected = True
                return tower

    def clear_selection():
        for tower in tower_group:
            tower.selected = False

    def runner():
        nonlocal run
        nonlocal placing_towers
        nonlocal selected_tower
        last_enemy_spawn = pg.time.get_ticks()
        score = 0
        next_level_ready = False  # **Flaga gotowości do następnego poziomu**
        current_map = 1  # **Zmiana mapy co 6 poziomów**

        while run:
            score += 1
            clock.tick(c.FPS)
            screen.fill("grey100")
            world.draw(screen)
            enemy_group.draw(screen)
            spots_group.draw(screen)
            enemy_group.update(world)
            tower_group.update(enemy_group)
            for tower in tower_group:
                tower.draw(screen)
            draw_text("health:", text_font, "grey100", 0, 0)
            draw_text(str(world.health), text_font, "grey100", 0, 30)
            draw_text("money:", text_font, "grey100", 0, 60)
            draw_text("level:", text_font, "grey100", 0, 120)
            draw_text(str(world.level), text_font, "grey100", 0, 150)

            if not next_level_ready:
                if pg.time.get_ticks() - last_enemy_spawn > c.SPAWN_COOLDOWN:
                    if world.spawned_enemies < len(world.enemy_list):
                        enemy_type = world.enemy_list[world.spawned_enemies]
                        enemy = Enemy(enemy_type, world.waypoints, enemy_images)
                        enemy_group.add(enemy)
                        world.spawned_enemies += 1
                        last_enemy_spawn = pg.time.get_ticks()

                all_enemies_reached = all(enemy.reached_goal for enemy in enemy_group)
                if world.spawned_enemies == len(world.enemy_list) and all_enemies_reached:
                    next_level_ready = True

            if next_level_ready:
                draw_text("Next Level Available", large_font, "red", c.SCREEN_WIDTH // 2, c.SCREEN_HEIGTH // 2)
                if next_level_button.draw(screen):
                    next_level_ready = False
                    world.level += 1
                    world.enemy_list = []
                    if world.level % 6 == 1:
                        current_map = (world.level - 1) // 6 + 1
                    with open(f"assets/points/points{current_map}.tmj") as file:
                        world_data = json.load(file)
                    world.level_data = world_data
                    world.waypoints = []
                    world.process_data()
                    world.process_enemies()
                    world.original_image = map_images.get(str(current_map))
                    world.image = pg.transform.rotate(world.original_image, world.angle)
                    world.spawned_enemies = 0
                draw_next_button_text(next_level_button, "Next Level", text_font, "black")

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
            if selected_tower and selected_tower.level < selected_tower.maxlevel:
                if upgrade_button.draw(screen):
                    selected_tower.upgrade()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False
                if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                    click_pos = pg.mouse.get_pos()
                    if click_pos[0] < c.SCREEN_WIDTH and click_pos[1] < c.SCREEN_HEIGTH:
                        actual_place = check_for_spot(click_pos)
                        selected_tower = None
                        clear_selection()
                        if placing_towers and actual_place:
                            create_tower(actual_place)
                        else:
                            selected_tower = select_tower(click_pos)

            pg.display.flip()
        with open("scores/scores.json", "r") as file:
            existing_scores = json.load(file)
        existing_scores.append(score)
        existing_scores.sort(reverse=True)
        with open("scores/scores.json", "w") as file:
            json.dump(existing_scores, file)

    runner()
