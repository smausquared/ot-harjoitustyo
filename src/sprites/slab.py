import pygame


class Slab(pygame.sprite.Sprite):
    """Slabs for more compact blocks to place in the air.

    Atrributes:
        x: X-coordinate of the block.

        y: Y-coordinate of the block.

        image: Slab texture.

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
            slab = pygame.image.load("src/assets/slab.png")
        except FileNotFoundError:
            slab = pygame.image.load("assets/slab.png")
        self.image = slab
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
