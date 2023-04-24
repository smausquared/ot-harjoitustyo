import pygame
class Grass(pygame.sprite.Sprite): # walk on grass!
    def __init__(self, x, y): # pylint: disable=invalid-name
        super().__init__()
        try:
            grass = pygame.image.load("src/assets/grass.png")
        except FileNotFoundError:
            grass = pygame.image.load("assets/grass.png")
        self.image = grass
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

    def draw(self, screen):
        screen.blit(self.image,self.rect)
