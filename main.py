import pygame as pg
import consts as c
from enemy import Enemy
from map import Map
from button import Button
from towers.tower import Tower


pg.init()
clock = pg.time.Clock()


screen = pg.display.set_mode((c.SCREEN_WIDTH + c.SIDE_PANEL,c.SCREEN_HEIGTH))
pg.display.set_caption("Tower Defense")
run = True
waypoints = [
    (100,100),
    (1100,100),
    (100,700),
    (1100,700)
]
tower_sheet = pg.image.load("toweranimation.png").convert_alpha()
tower_image = pg.image.load("t1.png").convert_alpha()
enemy_image = pg.image.load("e1.png").convert_alpha()
tower_button_img = pg.image.load("towerbutton.png").convert_alpha()
cancel_button_img = pg.image.load("cancelbutton.png").convert_alpha()

placing_towers = False
selected_towers = None


enemy_group = pg.sprite.Group()
tower_group = pg.sprite.Group()


enemy = Enemy(waypoints,enemy_image)
enemy_group.add(enemy)

tower_button = Button(c.SCREEN_WIDTH + 30, 120, tower_button_img)
cancel_button = Button(c.SCREEN_WIDTH + 160, 120, cancel_button_img)

def create_tower(click_pos):
    tower = Tower(click_pos, tower_sheet)
    tower_group.add(tower)


while run:
    clock.tick(c.FPS)

    screen.fill("grey100")

    pg.draw.lines(screen, "grey0", False, waypoints)

    enemy_group.update()
    for tower in tower_group:
        tower.draw(screen)

    enemy_group.draw(screen)
    tower_group.update(enemy_group)

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
