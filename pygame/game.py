import pygame
pygame.init()

screen_width = 800
screen_height = 600

WINDOW = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Boom Sabogsss")

white = (100, 100, 100)
player_x = 100
player_y = 100
player_speed_x = 1
player_speed_y = 1

enemy_x = 100
enemy_y = 100

enemy_speed_x = 2
enemy_speed_y = 2

#player display image
player1 = pygame.image.load("optimus prime.png")
player1 = pygame.transform.scale(player1, (player_x, player_y))

#enemy player display image
enemy_player = pygame.image.load("megatron.png")
enemy_player = pygame.transform.scale(enemy_player, (enemy_x, enemy_y))

gameRunning = True
while gameRunning == True:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            gameRunning = False

    #display the image of player
    WINDOW.blit(player1, (player_x, player_y))

    WINDOW.blit(enemy_player, (enemy_x, enemy_y))
    pygame.display.update()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed_x
    elif keys[pygame.K_RIGHT]:
        player_x += player_speed_x
    elif keys[pygame.K_UP]:
        player_y -= player_speed_y
    elif keys[pygame.K_DOWN]:
        player_y += player_speed_y
        
    WINDOW.fill(white)
pygame.quit()
