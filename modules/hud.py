import pygame


class Hud:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font("assets/font1.ttf", 32)
        self.score = 0
        self.lives = 3
        self.visibility = True

        self.render_texts()

    def update(self):
        def calculate_position(text):
            return (
                self.screen.get_width() - text.get_width() - 20,
                10,
            )

        self.render_texts()
        self.screen.blit(self.score_text, (10, 10))
        self.screen.blit(self.lives_text, (10, 50))
        self.screen.blit(
            self.title_text,
            calculate_position(self.title_text),
        )

    def render_texts(self):
        self.title_text = self.font.render(
            "Hungry Moneky v0.1",
            True,
            (255, 255, 0),
        )
        self.score_text = self.font.render(
            f"Score: {self.score}",
            True,
            (255, 255, 255),
        )
        self.lives_text = self.font.render(
            f"Lives: {self.lives}",
            True,
            (255, 255, 255),
        )

    def render(self):
        if self.visibility:
            self.update()

    def hide(self):
        self.visibility = False

    def decreaseLives(self):
        self.lives -= 1
        self.update()
        if self.lives < 1:
            self.lives = 0
