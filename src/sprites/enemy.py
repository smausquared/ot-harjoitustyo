from random import choice
import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x_coord, y_coord):
        super().__init__()
        self.speed = 3
        try:
            self.image = pygame.image.load("src/assets/enemy.png")
        except FileNotFoundError:
            self.image = pygame.image.load("assets/enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x_coord, y_coord+(self.image.get_height()/2))
        self.direction = choice([-1,1]) # for pathfinding and not running off a cliff
        self.vision_ground = pygame.Rect(0,0, 20, 20)
        self.vision_walls = pygame.Rect(0,0,40,20)

    def move(self, obstacles):
        delta_x = 0
        self.check_path(obstacles)
        self.vision_ground.center=(self.rect.centerx + 64 * self.direction, self.rect.centery + 40)
        self.vision_walls.center = (self.rect.centerx + 40*self.direction, self.rect.centery)
        delta_x += self.speed * self.direction
        self.rect.x += delta_x

    def check_path(self, obstacles):
        flip_ground = True
        flip_walls = False
        for obstacle in obstacles:
            if self.vision_ground.colliderect(obstacle.rect):
                flip_ground = False

            if self.vision_walls.colliderect(obstacle.rect):
                flip_walls = True


        if flip_ground or flip_walls:
            self.direction *= -1
    
    def attack(self,ghost):
        if pygame.sprite.collide_rect(self, ghost):
            ghost.take_damage()
