import pygame


class Grass(pygame.sprite.Sprite):
    """Grass to serve as the ground to walk on.

        Atrributes:
            x: X-coordinate of the block.

            y: Y-coordinate of the block.

            image: Grass texture.

            rect: Collision checking rectangle.

            rect.center: Center of the rectangle.
    """

    def __init__(self, x, y):  # pylint: disable=invalid-name
        """Constructor of the class.

        Args:
        x {integer} -- X-coordinate of the block.

        y {integer} -- Y-coordinate of the block.
        """
        super().__init__()
        try:
            grass = pygame.image.load("src/assets/grass.png")
        except FileNotFoundError:
            grass = pygame.image.load("assets/grass.png")
        self.image = grass
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
