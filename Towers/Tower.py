import pygame
class Tower:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.range = 100
        self.damage = 10
        self.attack_speed = 1
        self.target = None
        self.color = (255,0,0)

    def find_target(self, enemies):
        closest_enemy = None
        closest_dist = self.range

        for enemy in enemies:
            dist = ((self.x - enemy.x) ** 2 + (self.y - enemy.y) ** 2) ** 0.5
            if dist < closest_dist:
                closest_enemy = enemy
                closest_dist = dist

        if closest_enemy:
            self.target = closest_enemy

    def attack(self,screen):
        if self.target:
            self.target.health -= self.damage
            pygame.draw.circle(screen,self.color,(self.x,self.y + 12), 2)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), 10)
