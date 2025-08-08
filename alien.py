# import pygame
# pygame.init()

# screen = pygame.display.set_mode((800,600))

# pygame.display.set_caption("UFO Mover")

# clock = pygame.time.Clock()
# ufo_speed = 5
# ufo_image = pygame.image.load("ufo.png")
# ufo_rect = ufo_image.get_rect()
# ufo_rect.topleft = (30,30)

# running = True

# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_LEFT]:
#         ufo_rect.x -= ufo_speed
#     if keys[pygame.K_RIGHT]:
#         ufo_rect.x += ufo_speed
#     if keys[pygame.K_UP]:
#         ufo_rect.y -= ufo_speed
#     if keys[pygame.K_DOWN]:
#         ufo_rect.y += ufo_speed

#     if ufo_rect.left < 0:
#         ufo_rect.left = 0
#     if ufo_rect.right > 800:
#         ufo_rect.right = 800
#     if ufo_rect.top < 0:
#         ufo_rect.top = 0
#     if ufo_rect.bottom > 600:
#         ufo_rect.bottom = 600

#     screen.fill((0, 0, 0))
#     screen.blit(ufo_image, ufo_rect.topleft)
#     pygame.display.flip()
#     clock.tick(60)

# pygame.quit()

import pygame
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("UFO Mover")

clock = pygame.time.Clock()
ufo_speed = 5


ufo_image = pygame.image.load("ufo.png")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        ufo_rect.x -= ufo_speed
    if keys[pygame.K_RIGHT]:
        ufo_rect.x += ufo_speed
    if keys[pygame.K_UP]:
        ufo_rect.y -= ufo_speed
    if keys[pygame.K_DOWN]:
        ufo_rect.y += ufo_speed

    # Keep inside screen
    if ufo_rect.left < 0: ufo_rect.left = 0
    if ufo_rect.right > 800: ufo_rect.right = 800
    if ufo_rect.top < 0: ufo_rect.top = 0
    if ufo_rect.bottom > 600: ufo_rect.bottom = 600

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 255, 0), ufo_rect)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()