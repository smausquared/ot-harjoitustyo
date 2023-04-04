import pygame

class Ghost(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        super().__init__()
        ghost = pygame.image.load("erkkikummitus.png")
        self.ghost = pygame.transform.scale(ghost, (int(0.7*ghost.get_width()), int(0.7*ghost.get_height())))
        self.speed = speed
        self.rect = self.ghost.get_rect()
        self.rect.center = (x, y)

    def move(self, right, left):
        dx = 0
        dy = 0
        if right:
            dx += self.speed
        if left:
            dx -= self.speed
        
        self.rect.x += dx
        self.rect.y += dy

