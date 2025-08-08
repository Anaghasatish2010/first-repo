import pygame
pygame.init()

screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()

class RocketShipSprite (pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        frame1 = pygame.transform.scale(pygame.image.load("frame1.png").convert_alpha(), (132,132))
        frame2 = pygame.transform.scale(pygame.image.load("frame2.png").convert_alpha(), (132,132))
        frame3 = pygame.transform.scale(pygame.image.load("frame3.png").convert_alpha(), (132,132))
        frame4 = pygame.transform.scale(pygame.image.load("frame4.png").convert_alpha(), (132,132))

        self.frames = [frame1, frame2, frame3, frame4]
        self.current_frame = 0
        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect(topleft=(x,y))
        self.speed = 5
    def move(self):
        self.rect.y -= self.speed

        if self.rect.y < 0:
            self.rect.y = 600

        self.current_frame += 1
        if self.current_frame >= len(self.frames):
            self.current_frame = 0
            self.image = self.frames[self.current_frame]
rocket_object = RocketShipSprite(375,550)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    rocket_object.move()

    screen.fill((0,0,0))

    screen.blit(rocket_object.image, rocket_object.rect)

    pygame.display.flip()
    clock.tick(30)
pygame.quit()

        