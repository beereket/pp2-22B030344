import pygame, sys

h, w = 1280, 720
display = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Circle')

FPS = 60
x, y = 100, 100
step = 20

clock = pygame.time.Clock()

while True:
    clock.tick(FPS)
    display.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    key = pygame.key.get_pressed()
    if key[pygame.K_UP] and y > 25:
        y -= step
    if key[pygame.K_DOWN] and y < 475:
        y += step
    if key[pygame.K_RIGHT] and x < 475:
        x += step
    if key[pygame.K_LEFT] and x > 25:
        x -= step


    pygame.draw.circle(display, 'red', (x, y), 25)
    pygame.display.update()
