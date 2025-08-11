import pygame

from modules.banana import Banana
from modules.hud import Hud
from modules.menu import Menu
from modules.monkey import Monkey


class MonkeyBoard:
    def __init__(
        self,
        screen: pygame.Surface,
        background_image: pygame.Surface,
        screen_width: int,
        screen_height: int,
    ):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.hud = Hud(screen)
        self.menu = Menu(screen, screen_width, screen_height)
        self.monkey = Monkey(screen, screen_width, screen_height)
        self.banana = Banana(screen, screen_width, screen_height, self.hud)
        self.background_image = background_image

    def update(self, events: list[pygame.event.Event]):
        self.screen.blit(self.background_image, (0, 0))
        keys = pygame.key.get_pressed()

        for event in events:
            if event.type == pygame.KEYDOWN and self.menu.visibility:
                print("Game Started")
                self.monkey.visibility = True
                self.banana.visibility = True
                self.hud.lives = 3
                self.hud.score = 0
                self.menu.hide()

        if self.monkey.visibility:
            self.monkey.handle_keys(keys)
            self.banana.move()

        if self.monkey.rect.colliderect(self.banana.rect):
            self.banana.respawn()
            self.hud.score += 1
            print("Score: ", self.hud.score)
            self.hud.update()

        if self.hud.lives == 0:
            self.banana.visibility = False
            self.monkey.visibility = False
            self.menu.show_game_over_menu()

        self.hud.render()
        self.monkey.render()
        self.banana.render()

        if self.menu.visibility and not self.hud.lives == 0:
            self.menu.show_start_menu()

        pygame.display.update()
