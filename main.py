import pygame, sys 
from settings import *
from level import Level

pygame.init()
screen_width = 1200
screen_height = 700
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
level = level(level_map,screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill('black')
    level.run()
    

    pygame.display.update()
    clock.tick(60)