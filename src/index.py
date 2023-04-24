import pygame
from level import Level
from game_loop import Gameloop
from sprites.ghost import Ghost

def main():
# initialization of gameloop components
    screen = pygame.display.set_mode((1280, 720))
    level = Level(0)
    pygame.display.set_caption("Ghost game")
    clock = pygame.time.Clock()
    ghost = Ghost(150, 630, 1) # the level.py module will handle this in time
    pygame.init()
    game_loop = Gameloop(ghost, level, screen, clock)
    game_loop.start()

if __name__ == "__main__":
    main()
