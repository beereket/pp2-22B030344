import pygame
from pygame.locals import *
import random

class Car(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.screen_width = self.screen_rect.right
        self.screen_height = self.screen_rect.bottom

        self.image = pygame.transform.scale(pygame.image.load('images/redcar.png'), (60, 120))
        self.rect =self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        key = pygame.key.get_pressed()
        if self.rect.top > 0:
            if key[K_UP]:
                self.rect.move_ip(0, -5)
        if self.rect.bottom < self.screen_height:
            if key[K_DOWN]:
                self.rect.move_ip(0,5)

        if self.rect.left > 0:
            if key[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < self.screen_width:
            if key[K_RIGHT]:
                self.rect.move_ip(5, 0)

    def draw(self):
        self.screen.blit(self.image, self.rect)

class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.screen_width = self.screen_rect.right
        self.screen_height = self.screen_rect.bottom

        self.image = pygame.transform.scale(pygame.image.load('images/greencar.png'), (60, 120))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, self.screen_width-40), 0)
        self.score = 0

    def draw(self):
        self.screen.blit(self.image, self.rect)
    def move(self, speed):
        self.rect.move_ip(0, speed)
        if (self.rect.top > self.screen_height):
            self.rect.top = 0
            self.rect.center = (random.randint(40, self.screen_width - 40), 0)
            self.score += 1

class CoinGenerate(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.screen_width = self.screen_rect.right
        self.screen_height = self.screen_rect.bottom

        self.image = pygame.transform.scale(pygame.image.load('images/coin.png'), (40, 40))
        self.rect =self.image.get_rect()
        self.rect.center = (random.randint(40, self.screen_width-40), random.randint(40, self.screen_height-40))

    def NextOne(self):
        self.rect.center = (random.randint(40, self.screen_width - 40), random.randint(40, self.screen_height - 40))
    def draw(self):
        self.screen.blit(self.image, self.rect)

class MoneyGenerate(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.screen_width = self.screen_rect.right
        self.screen_height = self.screen_rect.bottom

        self.image = pygame.transform.scale(pygame.image.load('images/money.png'), (40, 40))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, self.screen_width - 40), random.randint(40, self.screen_height - 40))

    def NextOne(self):
        self.rect.center = (random.randint(40, self.screen_width - 40), random.randint(40, self.screen_height - 40))
    def draw(self):
        self.screen.blit(self.image, self.rect)
