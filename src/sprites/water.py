import pygame

class Water(pygame.sprite.Sprite):
    """Water at the bottom of the level.

        Atrributes:
            x: X-coordinate of the block.

            y: Y-coordinate of the block.

            image: Water texture.

            rect: Collision checking rectangle.

            rect.center: Center of the rectangle.
    """

    def __init__(self, x_coord, y_coord):
        """Constructor of the class.

        Args:
        x_coord {integer} -- X-coordinate of the block.

        y_coord {integer} -- Y-coordinate of the block.
        """
        super().__init__()
        try:
            water = pygame.image.load("src/assets/water.png")
        except FileNotFoundError:
            water = pygame.image.load("assets/water.png")
        self.image = water
        self.rect = self.image.get_rect()
        self.rect.center = (x_coord, y_coord)

    def attack(self,ghost):
        if pygame.sprite.collide_rect(self, ghost):
            ghost.lives = 0
            ghost.take_damage()
