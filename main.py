import pygame as pg
import json
from button import Button
import consts as c
from runner import play
pg.init()
clock = pg.time.Clock()


screen = pg.display.set_mode((c.SCREEN_WIDTH + c.SIDE_PANEL,c.SCREEN_HEIGTH))
pg.display.set_caption("Tower Defense")
run = True

start_image = pg.image.load("assets/menustart.png")
leaderboard_image = pg.image.load("assets/menuleaderboard.png")
exit_image = pg.image.load("assets/menuexit.png")

start_button = Button(c.SCREEN_WIDTH//2, c.SCREEN_HEIGTH//3 - 150, start_image)
leaderboard_button = Button(c.SCREEN_WIDTH//2, c.SCREEN_HEIGTH//3 * 2 - 150, leaderboard_image)
exit_button = Button(c.SCREEN_WIDTH//2, c.SCREEN_HEIGTH - 150, exit_image)


while run:
    clock.tick(c.FPS)

    screen.fill("grey100")

    if start_button.draw(screen):
        play()
    if leaderboard_button.draw(screen):
        print("todo")
    if exit_button.draw(screen):
        run = False

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    pg.display.flip()
