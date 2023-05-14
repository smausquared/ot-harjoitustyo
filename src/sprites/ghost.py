import pygame


class Ghost(pygame.sprite.Sprite):
    """Class to represent the player character.

    Attributes:
        image: Image of the ghost.
        alive: For keeping track whether the player is alive.
        timer: Timer for the update-method.
        flip: Attribute for flipping the player's image based on movement direction.
        scroll_area: Attribute for determining how far near the edges the player 
        has to move before the stage starts scrolling.
        speed_x: The horizontal speed of the player.
        speed_y: The vertical speed of the player.
        jumping: Tracking if the player is jumping.
        in_air: Tracking if the player is in the air.
        rect: Rectangle for checking collision with everything in the stage.
        rect.center: Center of the collision rectangle.
    """

    def __init__(self, x_coord, y_coord, speed):
        """Constructor of the class.

        Args:
            x: X-coordinate of the player.
            y: Y-coordinate of the player.
            speed: The player's speed.
        """
        super().__init__()
        try:
            ghost = pygame.image.load("src/assets/erkkikummitus.png")
        except FileNotFoundError:
            ghost = pygame.image.load("assets/erkkikummitus.png")
        self.image = pygame.transform.scale(ghost,
                                            (int(0.7*ghost.get_width()),
                                             int(0.7*ghost.get_height())))
        self.alive = True
        self.speed_timer = 0  # for speed decay cooldown
        self.damage_timer = 0
        self.flip = False  # flipping character direction based on movement
        self.lives = 3
        self.spoon_count = 0
        self.scroll_area = 450
        self.speed_x = speed
        self.speed_y = 0
        self.jumping = False
        self.in_air = True
        self.rect = self.image.get_rect()
        self.rect.center = (x_coord, y_coord)

    def move(self, right, left, level):
        """Method for handling player movement, checking collision and tracking scrolling.

        Args:
            right: If the input dictates that right movement shall commence.
            left: If the input dictates that left movement shall commence.
            level: The game level.

        Returns:
            integer: How much the level objects should scroll based on the player's movement. 
        """
        screen_scroll_x = 0
        screen_scroll_y = 0

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
            self.in_air = True  # prevent jumping in air
        self.speed_y += 0.68  # gravity
        self.speed_y = min(self.speed_y, 25)  # terminal velocity
        delta_y += self.speed_y

        delta_x, delta_y = self.check_collision(delta_x, delta_y, level)

        self.rect.x += delta_x
        self.rect.y += delta_y

        if self.rect.right > 1400 - self.scroll_area or \
                self.rect.left <= self.scroll_area:  # x scrolling
            self.rect.x -= delta_x
            screen_scroll_x = -delta_x

        if self.rect.y + self.rect.height//2 > 600 or \
                self.rect.y - self.rect.height//2 <= 200:  # y scrolling
            self.rect.y -= delta_y
            screen_scroll_y = -delta_y

        return (screen_scroll_x, screen_scroll_y)

    def update(self):
        """Method for updating the player's speed over time and 
        controlling how often the player can take damage.
        """

        if self.speed_x > 1 and self.speed_timer >= 100:
            self.speed_x *= 0.91
            self.speed_timer = 0
            if self.speed_x <= 1.5:  # making sure speed can't get lower than 1
                self.speed_x = 1
        self.damage_timer += 1
        self.speed_timer += 1

    def take_damage(self):
        """Function to take damage with an invunerability period shortly after.
        """
        if self.damage_timer >= 120 and self.lives > 0:
            self.lives -= 1
            self.damage_timer = 0
        if self.lives <= 0:
            self.alive = False
            self.speed_y = 0

    def check_collision(self, delta_x, delta_y, level):
        """Method for checking the player's collision with the level.
            Incidentally also a great place to check if the player is
            defeating an enemy by stomping them.
        Args:
            delta_x: Distance of how far the character would wish to move horizontally.
            delta_y: Distance of how far the character would wish to move vertically.
            level: The game level.

        Returns:
            integer: The delta_x and delta_y-values modified so that if the
            movement approaches a wall, the movement is cut short.
        """  # |
        for tile in level.obstacle_group:  # added larger buffer v for x-collision due to bugs
            if tile.rect.colliderect(self.rect.x + (delta_x + delta_x * 0.2), self.rect.y,
                                     self.rect.width, self.rect.height):  # x
                delta_x = 0
            if tile.rect.colliderect(self.rect.x, self.rect.y + delta_y,
                                     self.rect.width, self.rect.height):  # y
                if self.speed_y < 0:  # for bumping thy head upon the dastardly roof
                    self.speed_y = 0
                    delta_y = tile.rect.bottom - self.rect.top + 0.68

                elif self.speed_y >= 0:  # for planting thy feet on the ground
                    self.speed_y = 0
                    self.in_air = False
                    delta_y = tile.rect.top - self.rect.bottom - 0.68

        for enemy in level.enemy_group:
            if enemy.rect.colliderect(self.rect.x, self.rect.y + delta_y,
                                      self.rect.width, self.rect.height) and self.speed_y > 1:
                enemy.kill()

        return delta_x, delta_y
