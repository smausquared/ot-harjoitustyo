import pygame


class Gameloop:
    """The main game loop.

    Attributes:
        ghost: The player character.
        level: The game level.
        right: To track keyboard input for right movement.
        left: To track keyboard input for left movement.
        running: To turn the while-loop on or off.
        screen: The game window screen.
        clock: The game clock.
    """

    def __init__(self, ghost, level, screen, clock):
        """Constructor for the class.

        Args:
            ghost: The player character.
            level: The game level.
            screen: The game window screen.
            clock: The game clock.
        """
        self.ghost = ghost
        self.level = level
        self.right = None
        self.left = None
        self.running = None
        self.screen = screen
        self.clock = clock

    def start(self):
        """Method for starting the game loop.
        """
        self.right = False
        self.left = False
        self.running = True
        self.level.establish_groups()

        while self.running:
            self.clock.tick(60)
            self.screen.fill((173, 216, 230))

            if self.ghost.alive:
                scroll = self.ghost.move(
                    self.right, self.left, self.level)
                self.level.scroll_x = scroll[0]
                self.level.scroll_y = scroll[1]

            self.level.draw_level(self.screen)
            for spoon in self.level.spoon_group: # check spoon pickup
                spoon.update(self.ghost)
            self.ghost.update() # decrease speed over time
            self.screen.blit(pygame.transform.flip(self.ghost.image, # draw player
                                                   self.ghost.flip, False), self.ghost.rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.left = True
                    if event.key == pygame.K_d:
                        self.right = True
                    if event.key == pygame.K_w:
                        self.ghost.jumping = True

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        self.left = False
                    if event.key == pygame.K_d:
                        self.right = False
                    if event.key == pygame.K_w and self.ghost.alive:
                        self.ghost.jumping = False

            pygame.display.update()

        pygame.quit()
