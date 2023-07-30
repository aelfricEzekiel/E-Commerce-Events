import pygame

#Setting the screen of our game
window = pygame.display.set_mode((700, 500))

pygame.display.set_caption("Pogi sige na")
#Loads the image and stores it to the variable Ship
player_dog = pygame.image.load("dog.png")
player_dog = pygame.transform.scale(player_dog, (100, 100))

enemyCat = pygame.image.load("cat.png")
enemyCat = pygame.transform.scale(enemyCat, (100, 100))

player_x = 50
player_y = 100
player_speed_x = 1.5
player_speed_y = 1.5

enemy_x = 300
enemy_y = 300
enemy_speed_x = 1.5
enemy_speed_y = 1.5

gameRunning = True
while gameRunning == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameRunning = False
    #Provides background color to our screen
    window.fill((0, 0, 0))

    #Creates the hitbox for the player
    playerHitBox = pygame.Rect(player_x, player_y, 100, 100)
    pygame.draw.rect(window, (0, 255, 0), playerHitBox)

    #This will display the image of the ship to the screen
    window.blit(player_dog, (player_x, player_y))

    #Creates the hitbox for the enemy
    enemyHitBox = pygame.Rect(enemy_x, enemy_y, 100, 100)
    pygame.draw.rect(window, (255, 0, 0), enemyHitBox)

    #This will display the image of the enemy ship to the screen
    window.blit(enemyCat, (enemy_x, enemy_y))

    #This will check if the hitboxes are colliding with one another. Returns True or False
    bunggoanay = pygame.Rect.colliderect(playerHitBox, enemyHitBox)
    if bunggoanay == True:
        print("Ouch!!! sakit")


    #All of the changes to the screen will be updated by this line of code.
    pygame.display.update()

    #These lines of codes below allows inputs from keyboards
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player_x -= player_speed_x
    elif keys[pygame.K_d]:
        player_x += player_speed_x
    elif keys[pygame.K_w]:
        player_y -= player_speed_y
    elif keys[pygame.K_s]:
        player_y += player_speed_y
    elif keys[pygame.K_SPACE]:
        print("HAHAHAHAHA")

    keyz = pygame.key.get_pressed()
    if keyz [pygame.K_LEFT]:
        enemy_x -= enemy_speed_x 
    elif keyz[pygame.K_RIGHT]:
        enemy_x += enemy_speed_x 
    elif keyz[pygame.K_UP]:
        enemy_y -= enemy_speed_y
    elif keyz[pygame.K_DOWN]:
        enemy_y += enemy_speed_y
    elif keyz[pygame.K_KP_0]:
        print("hahaahaaaa")

        
pygame.quit()