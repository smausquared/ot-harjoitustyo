import pygame
from sprites.spoon import Spoon
from sprites.enemy import Enemy
from sprites.grass import Grass
from sprites.dirt import Dirt
from sprites.slab import Slab

TILESIZE = 64

class Level:
    def __init__(self, level):
        self.level = level
        self.scroll_x = 0
        self.scroll_y = 0
        self.spoon_group = pygame.sprite.Group()
        self.obstacle_group = pygame.sprite.Group()
        self.enemy_group = pygame.sprite.Group()
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

    def add_spoon(self, x_coord, y_coord):
        spoon = Spoon(x_coord*TILESIZE, y_coord*TILESIZE)
        self.spoon_group.add(spoon)
        self.everything_group.add(spoon)

    def add_enemy(self, x_coord, y_coord):
        enemy = Enemy(x_coord*TILESIZE, y_coord*TILESIZE)
        self.enemy_group.add(enemy)
        self.everything_group.add(enemy)

    def add_dirt(self, x_coord, y_coord):
        dirt = Dirt(x_coord*TILESIZE, y_coord*TILESIZE)
        self.obstacle_group.add(dirt)
        self.everything_group.add(dirt)

    def add_grass(self, x_coord, y_coord):
        grass = Grass(x_coord*TILESIZE, y_coord*TILESIZE)
        self.obstacle_group.add(grass)
        self.everything_group.add(grass)

    def add_slab(self, x_coord, y_coord):
        slab = Slab(x_coord*TILESIZE, y_coord*TILESIZE)
        self.obstacle_group.add(slab)
        self.everything_group.add(slab)

    def establish_groups(self):
        map_data = self.process_map_data("assets/level")
        for y_coord, row in enumerate(map_data):
            for x_coord, col in enumerate(row):
                if int(col) > 0:
                    if col == "1":
                        self.add_grass(x_coord, y_coord)
                    elif col == "2":
                        self.add_dirt(x_coord, y_coord)
                    elif col == "3":
                        self.add_spoon(x_coord, y_coord)
                    elif col == "4":
                        self.add_slab(x_coord, y_coord)
                    elif col == "5":
                        self.add_enemy(x_coord, y_coord)

    def draw_level(self, screen):
        for thing in self.everything_group:
            thing.rect.x += self.scroll_x
            thing.rect.y += self.scroll_y

            screen.blit(thing.image, (thing.rect.x, thing.rect.y))
