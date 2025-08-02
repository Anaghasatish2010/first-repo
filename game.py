# 

import pygame
pygame.init()

screen = pygame.display.set_mode([800, 600])
screen.fill((0, 0, 0)) 

running = True
rectangle = pygame.Rect((30, 30), (60, 100))  

while running:
    pygame.draw.rect(screen, (0, 128, 255), rectangle)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  

pygame.quit()