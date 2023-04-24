import pygame
from sprites.spoon import Spoon
TILESIZE = 64
class Level:
    def __init__(self, level_map): # temporary placings of spoons onto the level
        self.level = level_map
        self.spoon_group = pygame.sprite.Group()
        self.obstacle_group = pygame.sprite.Group()
        self.spoon_group.add(Spoon(350, 600))
        self.spoon_group.add(Spoon(400, 300))
        self.spoon_group.add(Spoon(450, 300))
        self.spoon_group.add(Spoon(470, 300))

    def process_map_data(self):
        pass
