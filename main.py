import nextSession
import thisSession
import sys

import pygame
from pygame.locals import QUIT

# initialized
pygame.init()
window_surface = pygame.display.set_mode((800, 600))
pygame.display.set_caption()
window_surface.fill((255, 255, 255))
window_surface.blit()
pygame.display.update()

# game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
