import pygame
class Dirt(pygame.sprite.Sprite):
    def __init__(self, x, y): # pylint: disable=invalid-name
        super().__init__()
        try:
            dirt = pygame.image.load("src/assets/dirt.png")
        except FileNotFoundError:
            dirt = pygame.image.load("assets/dirt.png")
        self.image = dirt
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

    def draw(self, screen):
        screen.blit(self.image,self.rect)
