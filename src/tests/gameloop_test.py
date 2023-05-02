import unittest
import pygame
from src.level import Level
from src.sprites.ghost import Ghost
from src.game_loop import Gameloop


class TestGameloop(unittest.TestCase):
    def setUp(self):
        pass

    def test_start(self):
        screen = pygame.display.set_mode((1280, 800))
        level = Level(1)
        clock = pygame.time.Clock()
        ghost = Ghost(550, 300, 1)
        game_loop = Gameloop(ghost, level, screen, clock)
        pygame.init()
        game_loop.start()
        self.assertLess(0, len(level.everything_group))
        self.assertEqual(False, game_loop.right)
