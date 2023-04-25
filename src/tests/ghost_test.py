import unittest
from src.level import Level
from src.sprites.ghost import Ghost


class TestMoving(unittest.TestCase):
    def setUp(self):
        self.level = Level(1)

    def test_moving_right_works(self):
        test_ghost = Ghost(150, 630, 1)
        test_ghost.move(True, False, self.level.obstacle_group)
        self.assertEqual(151, test_ghost.rect.center[0])


    def test_moving_left_works(self):
        test_ghost = Ghost(150, 630, 1)
        test_ghost.move(False, True,self.level.obstacle_group)
        self.assertEqual(149, test_ghost.rect.center[0])
