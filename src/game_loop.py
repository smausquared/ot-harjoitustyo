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
        self.font = pygame.font.SysFont("Arial", 30)
        self.ghost = ghost
        self.level = level
        self.right = None
        self.left = None
        self.running = None
        self.screen = screen
        self.clock = clock

    def draw_info(self):
        text = self.font.render(f"Lives: {self.ghost.lives}", True, (0,0,0))
        self.screen.blit(text, (30,30))

        text = self.font.render(f"Speed: {round(self.ghost.speed_x,2)}", True, (0,0,0))
        self.screen.blit(text, (30,60))

        text = self.font.render(f"Spoons: {self.ghost.spoon_count}", True, (0,0,0))
        self.screen.blit(text, (30,90))

        #text = self.font.render(f"Time: {self.timer//60}s", True, (0,0,0))
        #self.screen.blit(text, (100,200))

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
            for enemy in self.level.enemy_group:
                enemy.move(self.level.obstacle_group)
                enemy.attack(self.ghost)

            for spoon in self.level.spoon_group: # check spoon pickup
                spoon.update(self.ghost)
            self.ghost.update() # decrease speed over time
            self.screen.blit(pygame.transform.flip(self.ghost.image, # draw player
                                                   self.ghost.flip, False), self.ghost.rect)
            self.draw_info()

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
