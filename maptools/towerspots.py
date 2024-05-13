import pygame as pg
import json
import consts as c

pg.init()


image_path = "../assets/maps/map1.png"
image = pg.image.load(image_path)

screen = pg.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGTH))
pg.display.set_caption("Click Image")

click_coordinates = []

running = True
while running:
    screen.fill(0)
    screen.blit(image, (0, 0))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            click_coordinates.append(event.pos)

    pg.display.flip()

# Zapisanie współrzędnych kliknięć do pliku JSON
with open("../assets/towerspots/spots1.json", "w") as file:
    json.dump(click_coordinates, file)

pg.quit()
