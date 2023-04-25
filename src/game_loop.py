import pygame
class Gameloop: # gameloop handles rendering for now: perhaps #TODO renderer?
    def __init__(self, ghost, level, screen, clock):
        self.ghost = ghost
        self.level = level
        self.right = None
        self.left = None
        self.running = None
        self.screen = screen
        self.clock = clock

    def start(self):
        self.right = False
        self.left = False
        self.running = True
        self.level.establish_groups()

        while self.running:
            self.clock.tick(60)
            self.screen.fill((173, 216, 230))
            if self.ghost.alive:
                self.ghost.move(self.right, self.left, self.level.obstacle_group)
            for spoon in self.level.spoon_group: # draw spoons and check pickup
                spoon.draw(self.screen)
                spoon.update(self.ghost)
            for tile in self.level.obstacle_group:
                tile.draw(self.screen)
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
