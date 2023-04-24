import pygame
class Spoon(pygame.sprite.Sprite): # spoons increase the player's speed
    def __init__(self, x, y): # pylint: disable=invalid-name
        super().__init__()
        try:
            spoon = pygame.image.load("src/assets/spoon2.png")
        except FileNotFoundError:
            spoon = pygame.image.load("assets/spoon2.png")
        self.image = spoon
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

    def draw(self, screen):
        screen.blit(self.image,self.rect)

    def update(self, ghost): # check for collision with player
        if pygame.sprite.collide_rect(self, ghost):
            ghost.speed_x += 2.5
            self.kill()
