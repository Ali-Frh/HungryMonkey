import pygame

from modules import MonkeyBoard

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def main():
    pygame.init()
    clock = pygame.time.Clock()
    running = True
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    background_image = pygame.transform.scale(
        pygame.image.load("assets/garden.jpg"),
        (SCREEN_WIDTH, SCREEN_HEIGHT),
    )

    board = MonkeyBoard(
        screen,
        background_image,
        SCREEN_WIDTH,
        SCREEN_HEIGHT,
    )

    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False

        board.update(events)

        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()
