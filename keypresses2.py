import pygame
pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Pygame controller")

if pygame.joystick.get_count() >0:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
else:
    print("No controller found")
    exit()

player_pos_x = 400
player_pos_y = 300
player_speed = 5
player_color = (255,0,0)



clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.JOYBUTTONDOWN:
            if event.button == 2:
                player_color (0,0,255)
            elif event.type == pygame.JOYBUTTONUP:
                if event.button ==2:
                    player_color = (255,0,0)
    player_pos_x += int(joystick.get_axis(0) * player_speed)
    player_pos_y += int(joystick.get_axis(1) * player_speed)
            

    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, player_color, (player_pos_x, player_pos_y, 20))

    pygame.display.flip()
    clock.tick(60)
pygame.quit()