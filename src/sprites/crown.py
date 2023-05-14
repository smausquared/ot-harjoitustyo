import pygame


class Crown(pygame.sprite.Sprite):
    """Class for the crown at the end of the game. Picking it up will mean you won!

        Atrributes:
            x: X-coordinate of the spoon.
            y: Y-coordinate of the spoon.
            image: Spoon image.
            rect: Collision checking rectangle.
            rect.center: Center of the rectangle.
    """

    def __init__(self, x_coord, y_coord):
        """Constructor of the class.

        Args:
            x: X-coordinate of the crown.
            y: Y-coordinate of the crown.
        """
        super().__init__()
        try:
            crown = pygame.image.load("src/assets/kruunu.png")
        except FileNotFoundError:
            crown = pygame.image.load("assets/kruunu.png")
        self.image = crown
        self.rect = self.image.get_rect()
        self.rect.center = (x_coord, y_coord)

    def update(self, ghost):  # check for collision with player
        """Checks if the player is colliding with the crown.

        Args:
            ghost: The player class. 
        """
        if pygame.sprite.collide_rect(self, ghost):
            return True
        return False
