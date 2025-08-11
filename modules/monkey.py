import pygame


class Monkey:
    def __init__(self, screen, screen_width, screen_height):
        self.screen = screen
        self.image = pygame.image.load("assets/monkey.png")
        self.image = pygame.transform.scale(self.image, (150, 150))
        self.velocity = 5
        self.visibility = False
        self.rect = self.image.get_rect()
        self.rect.bottom = screen_height
        self.rect.left = screen_width // 2 - self.rect.width // 2
        self.position = [self.rect.left, self.rect.top]

    def handle_keys(self, keys):
        if keys[pygame.K_LEFT]:
            self.move_left()
        if keys[pygame.K_RIGHT]:
            self.move_right()

    def move_left(self):
        if self.rect.left > 5:
            print("be: POS: ", self.position[0], "Left: ", self.rect.left)
            self.position[0] -= self.velocity
            self.rect.left = self.position[0]
            print("after: POS: ", self.position[0], "Left: ", self.rect.left)

    def move_right(self):
        if self.rect.left < self.screen.get_width() - self.rect.width - 5:
            self.position[0] += self.velocity
            self.rect.left = self.position[0]

    def render(self):
        if self.visibility:
            self.screen.blit(self.image, self.rect)
            pygame.display.update()
