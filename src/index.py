import pygame
from level import Level
from game_loop import Gameloop
from sprites.ghost import Ghost


def main():
    # initialization of gameloop components
    screen = pygame.display.set_mode((1400, 1000))
    level = Level(1)
    pygame.display.set_caption("Ghost game")
    clock = pygame.time.Clock()
    ghost = Ghost(500, 599, 1)

    pygame.init()
    game_loop = Gameloop(ghost, level, screen, clock)
    if game_loop.start():  # restart function!
        main()


if __name__ == "__main__":
    main()
