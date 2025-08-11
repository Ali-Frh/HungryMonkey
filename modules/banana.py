import random

import pygame


class Banana:
    def __init__(
        self,
        screen,
        screen_width,
        screen_height,
        hud,
    ):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.image = pygame.image.load("assets/moz.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.velocity = 5
        self.visibility = False
        self.rect = self.image.get_rect()
        self.rect.top = 0
        self.rect.left = random.randint(0, screen_width - self.rect.width)
        self.position = [self.rect.left, self.rect.top]
        self.hud = hud

    def render(self):
        if self.visibility:
            self.screen.blit(self.image, self.rect)
            pygame.display.update()

    def move(self):
        if self.rect.top < self.screen_height:
            self.position[1] += self.velocity
            self.rect.top = self.position[1]
        else:
            self.hud.decreaseLives()
            self.respawn()

    def respawn(self):
        self.visibility = True
        self.rect.top = 0
        self.rect.left = random.randint(0, self.screen_width - self.rect.width)
        self.position = [self.rect.left, self.rect.top]
