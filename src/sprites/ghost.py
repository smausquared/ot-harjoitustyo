import pygame

class Ghost(pygame.sprite.Sprite):
    def __init__(self, x, y, speed): # pylint: disable=invalid-name
        super().__init__()
        ghost = pygame.image.load("erkkikummitus.png")
        self.ghost = pygame.transform.scale(ghost,
            (int(0.7*ghost.get_width()),
            int(0.7*ghost.get_height())))

        self.speed = speed
        self.rect = self.ghost.get_rect()
        self.rect.center = (x, y) # pylint: disable=invalid-name

    def move(self, right, left):
        delta_x = 0
        delta_y = 0
        if right:
            delta_x += self.speed
        if left:
            delta_x -= self.speed
        self.rect.x += delta_x
        self.rect.y += delta_y
