import unittest
import pygame
from sprites import ghost

class TestMoving(unittest.TestCase):
    def setUp(self):
        s = ghost.Ghost(150,630,1)

    def test_moving_works(self):
        s = ghost.Ghost(150,630,1)
        s.move(True,False)
        self.assertEqual(151,s.rect.center[0])
