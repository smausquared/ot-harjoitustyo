import unittest
import pygame
from src.level import Level
from src.sprites.spoon import Spoon
from src.sprites.ghost import Ghost

class TestSpoon(unittest.TestCase):
    def setUp(self):
        self.level = Level(1)
        self.ghost = Ghost(150, 400, 1)
        self.spoon = Spoon(151+self.ghost.rect.width//2,400)

    def test_spoon_pickup(self):
        self.spoon.update(self.ghost)
        self.assertEqual(3.5,self.ghost.speed_x)
