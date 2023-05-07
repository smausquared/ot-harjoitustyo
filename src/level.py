import pygame
from sprites.spoon import Spoon
from sprites.grass import Grass
from sprites.dirt import Dirt
from sprites.slab import Slab

TILESIZE = 64

class Level:
    def __init__(self, level):  # temporary placings of spoons onto the level
        self.level = level
        self.scroll_x = 0
        self.scroll_y = 0
        self.spoon_group = pygame.sprite.Group()
        self.obstacle_group = pygame.sprite.Group()
        self.everything_group = pygame.sprite.Group()

    def process_map_data(self, path):
        try:
            file = open(f'{path}{self.level}.txt', encoding="utf-8")
        except FileNotFoundError:
            file = open(f'src/{path}{self.level}.txt', encoding="utf-8")
        data = file.read()
        file.close()
        data = data.split('\n')
        game_map = []
        for row in data:
            game_map.append(list(row))

        return game_map

    def add_spoon(self, x, y):  # pylint: disable=invalid-name
        spoon = Spoon(x*TILESIZE, y*TILESIZE)
        self.spoon_group.add(spoon)
        self.everything_group.add(spoon)

    def add_dirt(self, x, y):  # pylint: disable=invalid-name
        dirt = Dirt(x*TILESIZE, y*TILESIZE)
        self.obstacle_group.add(dirt)
        self.everything_group.add(dirt)

    def add_grass(self, x, y):  # pylint: disable=invalid-name
        grass = Grass(x*TILESIZE, y*TILESIZE)
        self.obstacle_group.add(grass)
        self.everything_group.add(grass)

    def add_slab(self, x, y):  # pylint: disable=invalid-name
        slab = Slab(x*TILESIZE, y*TILESIZE)
        self.obstacle_group.add(slab)
        self.everything_group.add(slab)

    def establish_groups(self):
        map_data = self.process_map_data("assets/level")
        for y, row in enumerate(map_data):  # pylint: disable=invalid-name
            for x, col in enumerate(row):  # pylint: disable=invalid-name
                if int(col) > 0:
                    if col == "1":
                        self.add_grass(x, y)
                    elif col == "2":
                        self.add_dirt(x, y)
                    elif col == "3":
                        self.add_spoon(x, y)
                    elif col == "4":
                        self.add_slab(x, y)

    def draw_level(self, screen):
        for thing in self.everything_group:
            thing.rect.x += self.scroll_x
            thing.rect.y += self.scroll_y

            screen.blit(thing.image, (thing.rect.x, thing.rect.y))
