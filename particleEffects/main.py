import sys

import pygame

pygame.init()
pygame.display.set_caption("Particle Effects")
screen = pygame.display.set_mode((1000, 800))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((30, 30, 30))
    pygame.display.update()
    clock.tick(120)
