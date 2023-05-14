import pygame
import sqlite3

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
        timer: How long the player has been playing. Will be used for the leaderboard.
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
        self.ghost_original = ghost
        self.ghost = ghost
        self.level = level
        self.right = None
        self.left = None
        self.running = None
        self.completed = False
        self.endscreentimer = 0
        self.endscreentimeout = False
        self.screen = screen
        try:
            self.db = sqlite3.connect("src/leaderboard.db")
            self.leaderboard_data = self.db.execute("SELECT RANK() OVER (ORDER BY MIN(score)), \
                                name, MIN(score) FROM Players GROUP BY id").fetchall()
        except sqlite3.OperationalError:
            self.db = sqlite3.connect("leaderboard.db")
            self.leaderboard_data = self.db.execute("SELECT RANK() OVER (ORDER BY MIN(score)), \
                                name, MIN(score) FROM Players GROUP BY id").fetchall()
        self.db.isolation_level = None
        self.player_name = ""
        self.clock = clock
        self.timer = 0
        self.start_screen = True
        self.end_screen = False
        self.leaderboard = False
        self.start_menu_button = 0

    def draw_info(self):
        text = self.font.render(f"Lives: {self.ghost.lives}", True, (0,0,0))
        self.screen.blit(text, (30,30))

        text = self.font.render(f"Speed: {round(self.ghost.speed_x,2)}", True, (0,0,0))
        self.screen.blit(text, (30,60))

        text = self.font.render(f"Spoons: {self.ghost.spoon_count}", True, (0,0,0))
        self.screen.blit(text, (30,90))

        text = self.font.render(f"Time: {round(self.timer/60,1)}s", True, (0,0,0))
        self.screen.blit(text, (30,120))

    def show_leaderboard(self):
        # window
        self.screen.fill((173, 216, 230))
        pygame.draw.rect(self.screen, (20,20,20), pygame.Rect(400,0, 600, 1000))
        pygame.draw.rect(self.screen, (255,255,0), pygame.Rect(400,0, 600, 1000),3)

        text = self.font.render(f"Press ESC to return!", True, (255,255,0))
        self.screen.blit(text, (450,50))

        for i in range(len(self.leaderboard_data)):
            text = self.font.render(f"{self.leaderboard_data[i][0]}:   {self.leaderboard_data[i][1]}   {self.leaderboard_data[i][2]}s", True, (255,255,0))
            self.screen.blit(text, (450,100 + i * 30))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.leaderboard = False

    def handle_start_screen(self):
        # menu window and cursor
        self.screen.fill((173, 216, 230))
        pygame.draw.rect(self.screen, (20,20,20), pygame.Rect(400,200, 600, 600))
        pygame.draw.rect(self.screen, (255,255,0), pygame.Rect(400,200, 600, 600),3)

        text = self.font.render("Use arrow keys and enter to select!", True, (255,255,0))
        self.screen.blit(text, (450,230))

        text = self.font.render(">", True, (255,255,0))
        self.screen.blit(text, (530,400 + self.start_menu_button*100))

        # buttons
        text = self.font.render("START", True, (173, 216, 230))
        self.screen.blit(text, (650,400))
        pygame.draw.rect(self.screen, (255,255,0), pygame.Rect(630,390, 135, 55),3)

        text = self.font.render("LEADERBOARD", True, (173, 216, 230))
        self.screen.blit(text, (585, 500))
        pygame.draw.rect(self.screen, (255,255,0), pygame.Rect(565,490, 270, 55),3)

        text = self.font.render("QUIT", True, (173, 216, 230))
        self.screen.blit(text, (660, 600))
        pygame.draw.rect(self.screen, (255,255,0), pygame.Rect(630,590, 135, 55),3)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    if self.start_menu_button < 2:
                        self.start_menu_button += 1
                elif event.key == pygame.K_UP:
                    if self.start_menu_button > 0:
                        self.start_menu_button -= 1
                if event.key == pygame.K_RETURN:
                    if self.start_menu_button == 0:
                        self.start_screen = False
                    elif self.start_menu_button == 1:
                        self.leaderboard = True
                    elif self.start_menu_button == 2:
                        self.running = False

    def handle_end_screen(self):
        self.completed = True
        # menu window and cursor

        self.screen.fill((173, 216, 230))
        pygame.draw.rect(self.screen, (20,20,20), pygame.Rect(100,200, 900, 600))
        pygame.draw.rect(self.screen, (255,255,0), pygame.Rect(100,200, 900, 600),3)

        text = self.font.render\
        ("You win! Enter your name to submit", True, (255,255,0))
        self.screen.blit(text, (130,230))

        text = self.font.render("your score to the leaderboard!", True, (255,255,0))
        self.screen.blit(text, (130,260))

        text = self.font.render("... or press ESC to exit.", True, (255,255,0))
        self.screen.blit(text, (130,290))

        text = self.font.render(f"{self.player_name}", True, (255,255,0))
        self.screen.blit(text, (130,400))

        # ugly event handler </3
        # see line 251 for saving functionality.

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.completed = False
                self.running = False
            if event.type == pygame.KEYDOWN:
                if not self.endscreentimeout:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                    elif pygame.key.name(event.key) \
                    in "abcdefghijklmnopqrstuvwxyzöåä" and len(self.player_name) <= 15:
                        self.player_name += pygame.key.name(event.key).upper()
                    elif event.key == pygame.K_BACKSPACE and len(self.player_name) > 0:
                        self.player_name = self.player_name[:-1]
                    elif event.key == pygame.K_RETURN and len(self.player_name) > 0:
                        self.endscreentimeout = True

        if self.endscreentimeout:
            text = self.font.render \
            ("Score saved! Thanks for playing!", True, (255,255,0))
            self.screen.blit(text, (130,460))
            self.endscreentimer += 1
            if self.endscreentimer >= 240:
                self.running = False

    def start(self):
        """Method for starting the game loop.
        """
        self.right = False
        self.left = False
        self.running = True
        self.level.establish_groups()

        while self.running:
            self.clock.tick(60)

            if self.leaderboard:
                self.show_leaderboard()

            elif self.start_screen:
                self.handle_start_screen()

            elif self.end_screen:
                self.handle_end_screen()
            else:
                self.screen.fill((173, 216, 230))
                self.timer += 1

                if self.ghost.alive:
                    scroll = self.ghost.move(
                        self.right, self.left, self.level)
                    self.level.scroll_x = scroll[0]
                    self.level.scroll_y = scroll[1]
                else:
                    self.right = False
                    self.left = False
                    text = self.font.render("You died! Press R to try again!", True, (0,0,0))
                    self.screen.blit(text,
                                     (self.ghost.rect.centerx - 100, self.ghost.rect.centery - 100))

                self.level.draw_level(self.screen)
                for enemy in self.level.enemy_group:
                    enemy.move(self.level.obstacle_group)
                    enemy.attack(self.ghost)

                for spoon in self.level.spoon_group:
                    spoon.update(self.ghost)
                
                for crown in self.level.crown_group:
                    self.end_screen = crown.update(self.ghost)

                for water in self.level.water_group:
                    water.attack(self.ghost)

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
                        if event.key == pygame.K_r:
                            return True # return True if the player wishes to restart:
                                        # fulfills while-statement in index.py

                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_a:
                            self.left = False
                        if event.key == pygame.K_d:
                            self.right = False
                        if event.key == pygame.K_w and self.ghost.alive:
                            self.ghost.jumping = False

            pygame.display.update()

        pygame.quit()
        if self.completed:
            self.db.execute("INSERT INTO Players (name, score) VALUES (?, ?)",[self.player_name,(round(self.timer/60,1))])
