import pygame
pygame.mixer.init()

def play(path):
    pygame.mixer.music.load(path)
    pygame.mixer.music.play()
