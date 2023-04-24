import pygame
from sprites.spoon import Spoon
from sprites.grass import Grass
from sprites.dirt import Dirt

TILESIZE = 64
class Level:
    def __init__(self, level): # temporary placings of spoons onto the level
        self.level = level
        self.spoon_group = pygame.sprite.Group()
        self.obstacle_group = pygame.sprite.Group()
        self.obstacle_list = [] # testing collision with the sprite group proved inefficient
    def process_map_data(self, path):
        f = open(f'{path}{self.level}.txt','r')
        data = f.read()
        f.close()
        data = data.split('\n')
        game_map = []
        for row in data:
            game_map.append(list(row))

        return game_map

    def add_spoon(self,x,y):
        self.spoon_group.add(Spoon(x*TILESIZE,y*TILESIZE))

    def add_dirt(self,x,y):
        dirt = Dirt(x*TILESIZE,y*TILESIZE)
        self.obstacle_group.add(dirt)
        self.obstacle_list.append(dirt.rect)
    def add_grass(self,x,y):
        self.obstacle_group.add(Grass(x*TILESIZE,y*TILESIZE))

    def establish_groups(self):
        map_data = self.process_map_data("assets/level")
        for y in range(len(map_data)): # I don't know what that means, dearest pylint!
            for x in range(len(map_data[y])):
                if int(map_data[y][x])>0:
                    if map_data[y][x] == "1":
                        self.add_grass(x,y)
                    elif map_data[y][x] == "2":
                        self.add_dirt(x,y)
                    elif map_data[y][x] == "3":
                        self.add_spoon(x,y)
