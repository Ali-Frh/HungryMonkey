import pygame


class Menu:
    def __init__(self, screen, screen_width, screen_height):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = pygame.font.Font("assets/font1.ttf", 32)
        self.text = ""
        self.visibility = True

    def show_text(self, text):
        self.visibility = True
        self.text = self.font.render(text, True, (255, 255, 255))
        self.screen.blit(
            self.text,
            (
                self.screen_width // 2 - self.text.get_width() // 2,
                self.screen_height // 2,
            ),
        )

    def show_game_over_menu(self):
        self.show_text("Game Over, Press any key to restart")

    def show_start_menu(self):
        self.show_text("Press any key to start")

    def hide(self):
        self.visibility = False
        self.text = ""
