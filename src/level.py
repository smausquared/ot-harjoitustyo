import pygame
from sprites.spoon import Spoon
from sprites.grass import Grass
from sprites.dirt import Dirt

TILESIZE = 64
class Level:
    def __init__(self, level): # temporary placings of spoons onto the level
        self.level = level
        self.scroll = 0
        self.spoon_group = pygame.sprite.Group()
        self.obstacle_group = pygame.sprite.Group()
        self.everything_group = pygame.sprite.Group()

    def process_map_data(self, path):
        try:
            file = open(f'{path}{self.level}.txt',encoding="utf-8")
        except FileNotFoundError:
            file = open(f'src/{path}{self.level}.txt',encoding="utf-8")
        data = file.read()
        file.close()
        data = data.split('\n')
        game_map = []
        for row in data:
            game_map.append(list(row))

        return game_map

    def add_spoon(self,x,y):
        spoon = Spoon(x*TILESIZE,y*TILESIZE)
        self.spoon_group.add(spoon)
        self.everything_group.add(spoon)

    def add_dirt(self,x,y):
        dirt = Dirt(x*TILESIZE,y*TILESIZE)
        self.obstacle_group.add(dirt)
        self.everything_group.add(dirt)

    def add_grass(self,x,y):
        grass = Grass(x*TILESIZE,y*TILESIZE)
        self.obstacle_group.add(grass)
        self.everything_group.add(grass)

    def establish_groups(self):
        map_data = self.process_map_data("assets/level")
        for y in range(len(map_data)): # I don't know what that means, pylint!
            for x in range(len(map_data[y])):
                if int(map_data[y][x])>0:
                    if map_data[y][x] == "1":
                        self.add_grass(x,y)
                    elif map_data[y][x] == "2":
                        self.add_dirt(x,y)
                    elif map_data[y][x] == "3":
                        self.add_spoon(x,y)

    def draw_level(self, screen):
        for thing in self.everything_group:
            thing.rect.x += self.scroll
            screen.blit(thing.image, (thing.rect.x, thing.rect.y))
