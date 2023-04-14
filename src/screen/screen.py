import pygame
from sprites import ghost
pygame.init()
screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption("Ghost game")
clock = pygame.time.Clock()

ghost = ghost.Ghost(150,630,1) 
# the whole point of defining left and right 
# at this point is to change them later, what does pylint want???? :D
right = False # pylint: disable=invalid-name
left = False # pylint: disable=invalid-name
running = True # pylint: disable=invalid-name
while running: # pylint: disable=invalid-name
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False # pylint: disable=redefined-outer-name disable=invalid-name
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                left = True # pylint: disable=redefined-outer-name disable=invalid-name
            if event.key == pygame.K_d:
                right = True # pylint: disable=redefined-outer-name disable=invalid-name
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                left = False # pylint: disable=redefined-outer-name disable=invalid-name
            if event.key == pygame.K_d:
                right = False # pylint: disable=redefined-outer-name disable=invalid-name
    screen.fill((173,216,230))
    ghost.move(right,left)
    screen.blit(ghost.ghost, ghost.rect)

    pygame.display.update()
    clock.tick(60)
pygame.quit()
