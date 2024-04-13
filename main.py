import pygame
import sys
from Towers.Tower import Tower
pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gra Tower Defense")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

font = pygame.font.Font(None, 24)


def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)

def main_menu():
    pass

selected_tower = None

def game_screen():
    tower_buttons = []

    tower1_button = pygame.Rect(10, 50, 100, 30)
    tower_buttons.append(tower1_button)

    while True:
        screen.fill(WHITE)

        pygame.draw.rect(screen, GRAY, (0, 0, 120, HEIGHT))
        draw_text('Dostępne Wieże:', font, BLACK, screen, 10, 20)
        draw_text('Wieża 1', font, BLACK, screen, 20, 60)

        for button in tower_buttons:
            pygame.draw.rect(screen, BLACK, button, 2)

        for tower in towers:
            tower.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                global selected_tower
                if selected_tower is None:
                    for i, button in enumerate(tower_buttons):
                        if button.collidepoint(mouse_pos):
                            selected_tower = i
                            break
                else:
                    place_tower(mouse_pos)
                    selected_tower = None

        pygame.display.update()


def place_tower(position):
    print("place tower")
    tower = Tower(position[0], position[1])
    towers.append(tower)


def game_loop():

    pass

if __name__ == '__main__':
    towers = []

    main_menu()
    game_screen()
