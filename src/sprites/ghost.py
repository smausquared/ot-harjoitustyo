import pygame

class Ghost(pygame.sprite.Sprite): # player character
    def __init__(self, x, y, speed): # pylint: disable=invalid-name
        super().__init__()
        try:
            ghost = pygame.image.load("src/assets/erkkikummitus.png")
        except FileNotFoundError:
            ghost = pygame.image.load("assets/erkkikummitus.png")
        self.image = pygame.transform.scale(ghost,
                                        (int(0.7*ghost.get_width()),
                                         int(0.7*ghost.get_height())))
        self.alive = True
        self.timer = 0 # for speed decay cooldown
        self.flip = False # flipping character direction based on movement
        self.speed_x = speed
        self.speed_y = 0
        self.jumping = False
        self.in_air = True
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def move(self, right, left):  # handle movement of player
        delta_x = 0
        delta_y = 0
        if right:
            delta_x += self.speed_x
            self.flip = False
        elif left:  # "elif" so that movement continues if the player presses both left and right
            delta_x -= self.speed_x
            self.flip = True

        if self.jumping and not self.in_air:
            self.speed_y = -17
            self.jumping = False
            self.in_air = True # prevent jumping in air
        self.speed_y += 0.68 # gravity
        self.speed_y = min(self.speed_y, 25)  # terminal velocity
        delta_y += self.speed_y

        if self.rect.bottom + delta_y > 600:  # ground is at y = 600 before collision with level is added
            delta_y = 600 - self.rect.bottom
            self.in_air = False

        self.rect.x += delta_x
        self.rect.y += delta_y

    def update(self):  # I want the ghost's speed to increase from spoon pickups,
        # but decrease back to 1 over time
        decrease_cooldown = 100
        if self.speed_x > 1 and self.timer >= decrease_cooldown:
            self.speed_x *= 0.93
            self.timer = 0
            if self.speed_x <= 1.5: # making sure speed can't get lower than 1
                self.speed_x = 1
        self.timer += 1
