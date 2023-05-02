import unittest
from src.level import Level
from src.sprites.spoon import Spoon
from src.sprites.ghost import Ghost


class TestSpoon(unittest.TestCase):
    def setUp(self):
        pass

    def test_spoon_exists(self):
        level = Level(1)
        ghost = Ghost(150, 400, 1)
        level.add_spoon(151+ghost.rect.width//2, 400)
        self.assertEqual(1, len(level.spoon_group))

    def test_spoon_pickup(self):
        ghost = Ghost(150, 400, 1)
        spoon = Spoon(151+ghost.rect.width//2, 400)
        spoon.update(ghost)
        self.assertEqual(3.5, ghost.speed_x)
