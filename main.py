import pygame as pg
import json
from button import Button
import consts as c
from runner import play

pg.init()
clock = pg.time.Clock()

screen = pg.display.set_mode((c.SCREEN_WIDTH + c.SIDE_PANEL, c.SCREEN_HEIGTH))
pg.display.set_caption("Tower Defense")
run = True

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

while run:
    clock.tick(c.FPS)

    screen.fill("grey100")
    if not leaderboard_is_open and start_button.draw(screen):
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
