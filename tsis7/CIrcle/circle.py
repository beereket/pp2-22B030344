import pygame, sys

H, W = 700, 700
display = pygame.display.set_mode((H, W), pygame.RESIZABLE)
pygame.display.set_caption('Circle')

FPS = 60
x, y = 100, 100
R = 25
step = 20

clock = pygame.time.Clock()

while True:
    clock.tick(FPS)
    display.fill((255, 255, 255))
    
    rect = display.get_rect() 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    key = pygame.key.get_pressed()
    if key[pygame.K_UP] and y > rect.top + R:
        y -= step
    if key[pygame.K_DOWN] and y < rect.bottom - R:
        y += step
    if key[pygame.K_RIGHT] and x < rect.right - R:
        x += step
    if key[pygame.K_LEFT] and x > rect.left + R:
        x -= step


    pygame.draw.circle(display, 'red', (x, y), R)
    pygame.display.update()
