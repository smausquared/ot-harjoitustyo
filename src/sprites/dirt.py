import pygame


class Dirt(pygame.sprite.Sprite):
    """Dirt for walls and ground.

    Atrributes:
        x: X-coordinate of the block.

        y: Y-coordinate of the block.

        image: Dirt texture.

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
            dirt = pygame.image.load("src/assets/dirt.png")
        except FileNotFoundError:
            dirt = pygame.image.load("assets/dirt.png")
        self.image = dirt
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
