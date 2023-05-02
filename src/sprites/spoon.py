import pygame


class Spoon(pygame.sprite.Sprite):
    """Class to represent spoons in the game world for the 
    player to pick up to increase their speed.

        Atrributes:
            x: X-coordinate of the spoon.
            y: Y-coordinate of the spoon.
            image: Spoon image.
            rect: Collision checking rectangle.
            rect.center: Center of the rectangle.
    """

    def __init__(self, x, y):  # pylint: disable=invalid-name
        """Constructor of the class.

        Args:
            x: X-coordinate of the block.
            y: Y-coordinate of the block.
        """
        super().__init__()
        try:
            spoon = pygame.image.load("src/assets/spoon2.png")
        except FileNotFoundError:
            spoon = pygame.image.load("assets/spoon2.png")
        self.image = spoon
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self, ghost):  # check for collision with player
        """Checks if the player is colliding with the spoon, so that spoons may be picked up.

        Args:
            ghost: The player class. 
        """
        if pygame.sprite.collide_rect(self, ghost):
            ghost.speed_x += 2.5
            self.kill()
