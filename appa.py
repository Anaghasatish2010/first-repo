# 

import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

class AppaSprite(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        appa1 = pygame.transform.scale(pygame.image.load("appa1.png").convert_alpha(), (132,132))
        appa2 = pygame.transform.scale(pygame.image.load("appa2.png").convert_alpha(), (132,132))
        appa3 = pygame.transform.scale(pygame.image.load("appa3.png").convert_alpha(), (132,132))
        appa4 = pygame.transform.scale(pygame.image.load("appa4.png").convert_alpha(), (132,132))

        self.frames = [appa1, appa2, appa3, appa4]
        self.current_frame = 0
        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect(topleft=(x, y))

        self.speed = 5
        self.direction = [random.choice([-1, 1]), random.choice([-1, 1])] 

    def move(self):
     
        self.rect.x += self.direction[0] * self.speed
        self.rect.y += self.direction[1] * self.speed

        
        if self.rect.left < 0 or self.rect.right > 800:
            self.direction[0] *= -1
        if self.rect.top < 0 or self.rect.bottom > 600:
            self.direction[1] *= -1

        
        self.current_frame += 1
        if self.current_frame >= len(self.frames):
            self.current_frame = 0
        self.image = self.frames[self.current_frame]

rocket_object = AppaSprite(375, 300)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    rocket_object.move()

    screen.fill((0, 0, 0))
    screen.blit(rocket_object.image, rocket_object.rect)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
