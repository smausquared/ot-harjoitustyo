import unittest
from src.level import Level
from src.sprites.ghost import Ghost


class TestMoving(unittest.TestCase):
    def setUp(self):
        self.level = Level(1)

    def test_moving_right_works(self):
        test_ghost = Ghost(500, 630, 1)
        test_ghost.move(True, False, self.level)
        self.assertEqual(501, test_ghost.rect.center[0])

    def test_moving_left_works(self):
        test_ghost = Ghost(500, 630, 1)
        test_ghost.move(False, True,self.level)
        self.assertEqual(499, test_ghost.rect.center[0])

    def test_jumping_works(self):
        test_ghost = Ghost(500, 630, 1)
        test_ghost.in_air = False
        test_ghost.jumping = True
        test_ghost.move(False, False,self.level)
        self.assertLess(-17, test_ghost.speed_y)
