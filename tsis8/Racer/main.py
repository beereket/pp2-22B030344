import random, pygame, sys, time
from pygame.locals import *
pygame.init()

#colors
col_BLUE  = (0, 0, 255)
col_R = (255, 0, 0)
col_GR = (0, 255, 0)
col_BLACK = (0, 0, 0)
col_WH = (255, 255, 255)
COL_PRP = (230, 230, 250)

# display variables
display_width = 840
display_height = 650

# the size and color of background screen
display = pygame.display.set_mode((840, 650), RESIZABLE)
display.fill(col_WH)

# setting up the FPS
FPS = 60
fepes = pygame.time.Clock()
own_Speed = 5

# loading the images of the cars
car_Enemy = pygame.image.load('images/redcar.png')
car_Own = pygame.image.load('images/greencar.png')
bg = pygame.image.load("images/AnimatedStreet.png")

#fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, col_BLACK)

class coin_generation(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.img = pygame.transform.scale(pygame.image.load('images/coin.png'), (40,40))
        self.rect = self.img.get_rect()
        self.rect.center = (random.randint(150, display_width-150), random.randint(60, display_height-60))
        #setting up information about the coin

    def nextCoin(self):
        self.rect.center = (random.randint(150, display_width-200), random.randint(60, display_height-60))
        #generating random position for next coin
    def render(self, surface):
        surface.blit(self.img, self.rect)

class ownMovement(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.car = pygame.transform.scale(pygame.image.load('images/blucar.png'), (110, 110))
        self.rect = self.car.get_rect()
        self.rect.center = (600, 600)
        #setting up the player's car

    def move(self):
        key = pygame.key.get_pressed()
        if(self.rect.bottom < display_height):
            if key[K_DOWN]:
                self.rect.move_ip(0, 5)
        if(self.rect.top > 0):
            if key[K_UP]:
                self.rect.move_ip(0, -5)
        if (self.rect.right < display_width-138):
            if key[K_RIGHT]:
                self.rect.move_ip(5, 0)
        if (self.rect.left > 138):
            if key[K_LEFT]:
                self.rect.move_ip(-5, 0)
        #checking the input and moving the car
    def render(self,surface):
        surface.blit(self.car, self.rect)

class enemyMovement(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.car = pygame.transform.scale(pygame.image.load('images/greencar.png'), (45, 90))
            self.rect = self.car.get_rect()
            self.rect.center = (random.randint(138, display_width-138),0)
            #setting up the enemy cars

        def move(self):
            self.rect.move_ip(0, own_Speed)
            if(self.rect.bottom>display_width):
                self.rect.top = 0
                self.rect.center = (random.randint(138, display_width-138),0)
            #movement of the enemy cars and generation of its position
        def render(self, surface):
            surface.blit(self.car, self.rect)

current_Own = ownMovement()
current_Enemy = enemyMovement()
current_Coin = coin_generation()
#creating objects for the elements of the game

sprite_Coin = pygame.sprite.Group()
sprite_Coin.add(current_Coin)
sprite_Enemy = pygame.sprite.Group()
sprite_Enemy.add(current_Enemy)
sprite_All = pygame.sprite.Group()
sprite_All.add(current_Enemy)
sprite_All.add(current_Own)
#working with sprites of the objects

global collected
collected = 0
coins = 0
#counter for coins

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            if own_Speed > 5:
                pass
            else:
                own_Speed += 2

    for i in pygame.event.get():
        if i.type == QUIT:
            sys.exit()
    display.blit(bg, (0, 0))
    scores = font_small.render(str(coins), True, col_BLACK)
    display.blit(scores, (840-24, 10))


    # moves and redraws all sprites
    for entity in sprite_All:
        display.blit(entity.car, entity.rect)
        entity.move()
    for i in sprite_Coin:
        i.render(display)

    #check if collision with coin occurs and increase the coin counter if it does
    if pygame.sprite.spritecollideany(current_Own, sprite_Coin):
        current_Coin.nextCoin()
        coins+=1


    # to be run if collision occurs between player and pnemy
    if pygame.sprite.spritecollideany(current_Own, sprite_Enemy):
        pygame.mixer.Sound('sound/crash.mp3').play()
        time.sleep(0.7)

        display.fill(col_R)
        display.blit(game_over, (265, 280))
        pygame.display.update()

        for entity in sprite_All:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()
    pygame.display.update()
    fepes.tick(FPS)