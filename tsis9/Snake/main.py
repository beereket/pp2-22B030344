import pygame, sys, random
from pygame.locals import *
from point import Point
from Snake import *

pygame.init()
screen = pygame.display.set_mode((700, 700), RESIZABLE)
pygame.display.set_caption('Snake')
screenrect = screen.get_rect()

#CONST
FPS = pygame.time.Clock()
RED = 'red'
block = 25

#CountDown for Foods
time_event = pygame.USEREVENT + 1
pygame.time.set_timer(time_event, 1000)

def main():
    snake = Snake(screen)
    food = Food(screen ,5, 5)

    #CONST
    food_id = 0
    dx, dy = 0, 0
    CD = 7
    Score = 0
    DIFFICULITY = 5
    LEVEL = 0
    ScoreCounter = 0

    while True:
        screen.fill('black')

        # Score font
        score = pygame.font.SysFont("arial", 35).render("You Score: " + str(Score), True, 'white')
        screen.blit(score, (10, 10))

        # Level font
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
            if event.type == time_event:
                CD -= 1
                if CD == 0:
                    CD = 7
                    food.location.x = random.randint(0, screenrect.right // block - 1)
                    food.location.y = random.randint(0, screenrect.bottom // block - 1)
                    food_id = random.randint(0, 2)

        snake.move(dx, dy)

        #FOOD
        if snake.check_collision(food):

            food.location.x = random.randint(0, screenrect.right // block - 1)
            food.location.y = random.randint(0, screenrect.bottom // block - 1)
            CD = 7

            if food_id == 2:
                Score += 3
                ScoreCounter += 3
                for i in range(0, 3):
                    snake.body.append(
                        Point(snake.body[-1].x, snake.body[-1].y)
                    )
            else:
                Score += 1
                ScoreCounter += 1
                snake.body.append(
                    Point(snake.body[-1].x, snake.body[-1].y)
                )
            food_id = random.randint(0, 2)

        #LevelChecker
        if ScoreCounter > 3:
            ScoreCounter -= 4
            LEVEL += 1
            DIFFICULITY += 5

        #Draw
        snake.draw()
        draw_grid(screen)
        if food_id == 2: food.draw2()
        else: food.draw()

        if snake.game_over() and Score != 0:
            RePlay()

        pygame.display.flip()
        FPS.tick(DIFFICULITY)

def RePlay():
    while True:
        screen.fill(('red'))
        message = "You Lost! Press P-Play Again or Q-Quit"
        TEXT = pygame.font.SysFont("bahnschrift", 25).render(message, True, 'white')
        screen.blit(TEXT, [140, 350])
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