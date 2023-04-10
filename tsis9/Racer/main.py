import pygame, sys, time
from random import randint
from pygame.locals import *
from car import *

pygame.init()
SCREEN = pygame.display.set_mode((600, 800))
pygame.display.set_caption('Racer by Bereket')
background = pygame.image.load('images/AnimatedStreet.png')
background = pygame.transform.scale(background, (600, 800))

#COIN CD
time_event = pygame.USEREVENT + 1
pygame.time.set_timer(time_event, 1000)

#FPS
clock = pygame.time.Clock()
FPS = 60

#FONT
font = pygame.font.SysFont('Comic Sans MS', 30)

def main():
    # Game Objects
    COINS = 0
    SPEED = 5
    COIN_CONTROLLER = 0
    CD = 5
    Level = 0
    coin_id = random.randint(0, 2)

    # Sprites
    global M1, C1
    P1 = Car(SCREEN)
    E1 = Enemy(SCREEN)
    C1 = CoinGenerate(SCREEN)
    M1 = MoneyGenerate(SCREEN)

    # SPRITE GROUP
    # enemy
    enemies = pygame.sprite.Group()
    enemies.add(E1)
    # coin
    coins = pygame.sprite.Group()
    coins.add(C1)

    # money = 3 coin
    money = pygame.sprite.Group()
    money.add(M1)

    all_sprites = pygame.sprite.Group()
    all_sprites.add(P1)
    all_sprites.add(E1)
    all_sprites.add(C1)

    # RandomCoinID
    id = randint(0, 3)

    while True:
        #BACKGROUND
        SCREEN.blit(background, (0, 0))

        # Collected coins
        COINS_font = font.render(str(COINS), True, 'yellow')
        Level_font = font.render("Level: " +  str(Level), True, 'white')
        SCREEN.blit(Level_font, (10, 50))
        SCREEN.blit(COINS_font, (60, 10))
        SCREEN.blit(C1.image, (10, 10))

        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()

            if event.type == time_event:
                CD -= 1
                if CD == 0:
                    CD = 5
                    id = randint(0, 3)

        #INC LEVEL:
        if COIN_CONTROLLER > 4:
            COIN_CONTROLLER -= 5
            SPEED += 3
            Level += 1

        # Draw
        P1.draw()
        E1.draw()

        #Movement
        P1.move()
        E1.move(SPEED)

        if pygame.sprite.spritecollideany(P1, coins):
            COINS += 1
            CD = 5
            id = randint(0, 3)
            COIN_CONTROLLER += 1
            C1.NextOne()

        if pygame.sprite.spritecollideany(P1, money):
            COINS += 3
            CD = 5
            id = randint(0, 3)
            COIN_CONTROLLER += 3
            M1.NextOne()

        if id == 0:
            M1.draw()

        else:
            C1.draw()

        if pygame.sprite.spritecollideany(P1, enemies):
            pygame.mixer.Sound('sound/crash.mp3').play()
            time.sleep(0.5)

            pygame.display.update()
            for entity in all_sprites:
                entity.kill()
            RePlay()

        clock.tick(FPS)
        pygame.display.update()

def RePlay():
    while True:
        SCREEN.fill(('red'))

        message = "You Lost! Press P-Play Again or Q-Quit"
        TEXT = pygame.font.SysFont("bahnschrift", 25).render(message, True, 'white')

        SCREEN.blit(TEXT, [100, 350])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    return main()
                elif event.key == pygame.K_q:
                    sys.exit()
        pygame.display.update()






if __name__ == '__main__':
    main()
