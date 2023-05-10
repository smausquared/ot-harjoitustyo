import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x_coord, y_coord):
        super().__init__()
        self.speed = 3