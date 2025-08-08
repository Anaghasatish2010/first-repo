import pygame
pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Sound Example")

laser_sound = pygame.mixer.Sound("fire.mp3")

pygame.mixer.music.load("gamemusic.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                laser_sound.play()

screen.fill((0,0,0))
pygame.display.flip()