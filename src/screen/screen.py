import pygame
# indeed, this first go around the program is quite
# spaghetti-y. I promise that next week we'll have
# more clarity in the code, for now I just had to
# get something worth showing out the door.
# I'm going to familiarize myself with pygame more,
# next week it's not going to all be in one file :D

pygame.init()
screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption("Ghost game")
x = 150
y = 630
clock = pygame.time.Clock()

class Ghost(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        super().__init__()
        ghost = pygame.image.load("erkkikummitus.png")
        self.ghost = pygame.transform.scale(ghost, (int(0.7*ghost.get_width()), int(0.7*ghost.get_height())))
        self.speed = speed
        self.rect = self.ghost.get_rect()
        self.rect.center = (x, y)
    
    def move(self, right, left):
        dx = 0
        dy = 0
        if right:
            dx += self.speed
        if left:
            dx -= self.speed
        
        self.rect.x += dx
        self.rect.y += dy



ghost = Ghost(150, 630, 1)
right = False
left = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                left = True
            if event.key == pygame.K_d:
                right = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                left = False
            if event.key == pygame.K_d:
                right = False
    screen.fill((173,216,230))
    ghost.move(right,left)
    screen.blit(ghost.ghost, ghost.rect)

    pygame.display.update()
    clock.tick(60)
pygame.quit()
