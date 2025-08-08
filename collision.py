import pygame
pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Collision Example")

clock = pygame.time.Clock()

player = pygame.Rect(100,100,50,50)
item = pygame.Rect(300,300,30,30)
player_color = (0,128,255)
item_color = (0,128,255)

speed = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= speed
    if keys[pygame.K_RIGHT]:
        player.x += speed
    if keys[pygame.K_UP]:
        player.y -= speed
    if keys[pygame.K_DOWN]:
        player.y += speed

    player.clamp_ip(screen.get_rect())

    if player.colliderect(item):
        item_color = (0,255,255)
    else:
        item_color = (128,0,128)

    screen.fill((0,0,0))
    pygame.draw.rect(screen, player_color, player)
    pygame.draw.rect(screen, item_color, item)
    pygame.display.flip()
    clock.tick(30)

pygame.quit()