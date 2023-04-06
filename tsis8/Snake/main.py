import pygame, sys, random
from pygame.locals import *
from point import Point

pygame.init()
screen = pygame.display.set_mode((700, 700), RESIZABLE)
screenrect = screen.get_rect()

RED = 'red'

#CONST
block = 25
FPS = pygame.time.Clock()

class Snake():
    def __init__(self):
        self.body = [
            Point(
                x=screenrect.right // block // 2,
                y=screenrect.bottom // block // 2,
            ),
            Point(
                x=screenrect.right // block // 2 + 1,
                y=screenrect.bottom // block // 2,
            ),
        ]

    def draw(self):
        head = self.body[0]
        pygame.draw.rect(
            screen,
            'red',
            pygame.Rect(
                head.x * block,
                head.y * block,
                block,
                block,
            )
        )
        for body in self.body[1:]:
            pygame.draw.rect(
                screen,
                'white',
                pygame.Rect(
                    body.x * block,
                    body.y * block,
                    block,
                    block,
                )
            )

    def game_over(self):
        cordinate0 = self.body[0]
        for cordinate in self.body[1:]:
            if cordinate.x == cordinate0.x:
                if cordinate.y == cordinate0.y:
                    return True

    def move(self, dx, dy, size=block):
        for idx in range(len(self.body) - 1, 0, -1):
            self.body[idx].x = self.body[idx - 1].x
            self.body[idx].y = self.body[idx - 1].y
        # [Point(0, 1), Point(2, 5), Point(5, 9)]
        # [Point(0, 0), Point(0, 1), Point(2, 5)]
        self.body[0].x += dx
        self.body[0].y += dy

        if self.body[0].x > screenrect.right // block:
            self.body[0].x = 0
        elif self.body[0].x < 0:
            self.body[0].x = screenrect.right // size
        elif self.body[0].y < 0:
            self.body[0].y = screenrect.right // size
        elif self.body[0].y > screenrect.bottom // size:
            self.body[0].y = 0

    def check_collision(self, food):
        if food.location.x != self.body[0].x:
            return False
        if food.location.y != self.body[0].y:
            return False
        return True

def draw_grid():
    for x in range(0, screenrect.right, block):
        pygame.draw.line(screen, 'white', start_pos=(x, 0), end_pos=(x, screenrect.bottom), width=1)
    for y in range(0, screenrect.bottom, block):
        pygame.draw.line(screen, 'white', start_pos=(0, y), end_pos=(screenrect.right, y), width=1)

class Food:
    def __init__(self, x, y):
        self.location = Point(x, y)

    def draw(self):
        pygame.draw.rect(
            screen,
            'green',
            pygame.Rect(
                self.location.x * block,
                self.location.y * block,
                block,
                block,
            )
        )

while True:
    snake = Snake()
    food = Food(5, 5)
    dx, dy = 0, 0

    Score = 0
    DIFFICULITY = 5
    LEVEL = 0
    WAS = False #To avoid lvl problem
    while True:
        screen.fill('black')

        #Score
        score = pygame.font.SysFont("arial", 35).render("You Score: " + str(Score), True, 'white')
        screen.blit(score, (10, 10))

        #Level
        level = pygame.font.SysFont("arial", 35).render("You Level: " + str(LEVEL), True, 'white')
        screen.blit(level, (screenrect.centerx - 35, screenrect.top + 10))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and (dx != -1 or dy != 0):
                    dx, dy = 1, 0
                elif event.key == pygame.K_LEFT and (dx != 1 or dy != 0):
                    dx, dy = -1, 0
                elif event.key == pygame.K_UP and (dx != 0 or dy != 1):
                    dx, dy = 0, -1
                elif event.key == pygame.K_DOWN and (dx != 0 or dy != -1):
                    dx, dy = 0, 1

        snake.move(dx, dy)
        if snake.check_collision(food):
            snake.body.append(
                Point(snake.body[-1].x, snake.body[-1].y)
            )
            food.location.x = random.randint(0, screenrect.right // block - 1)
            food.location.y = random.randint(0, screenrect.bottom // block - 1)
            Score += 1
        if Score % 4 != 0:
            WAS = True
        if Score % 4 == 0 and Score != 0 and WAS:
            LEVEL += 1
            DIFFICULITY += 1
            WAS = False

        snake.draw()
        food.draw()
        draw_grid()
        
        if snake.game_over() and Score != 0:
            sys.exit()

        pygame.display.flip()
        FPS.tick(DIFFICULITY)
