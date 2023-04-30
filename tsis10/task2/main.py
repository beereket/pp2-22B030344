import sys, psycopg2
from pygame.locals import *
from assets.Snake import *
from config import *

pygame.init()
screen = pygame.display.set_mode((700, 700))
pygame.display.set_caption('Snake')
screenrect = screen.get_rect()

#Database connect
conn = psycopg2.connect(
            host=host,
            dbname=database,
            user=user,
            password=password,
            port=port
        )
cur = conn.cursor()

#TABLE
cur.execute(
   '''CREATE TABLE IF NOT EXISTS usertable(
   username varchar(100) NOT NULL,
   user_score int,
   user_level int
   )'''
)
conn.commit()

#CONST
FPS = pygame.time.Clock()
RED = 'red'
block = 25

#CountDown for Foods
time_event = pygame.USEREVENT + 1
pygame.time.set_timer(time_event, 1000)

def insertname(username):
   cur.execute(
      "INSERT INTO usertable VALUES('{}', 0, 0)".format(username)
   )
   conn.commit()

def upd(user, SCORE, LEVEL):
   cur.execute(
      "SELECT * FROM usertable WHERE username = '{}'".format(user)
   )
   row = cur.fetchone()
   cur.execute(
      "UPDATE usertable SET user_score = '{}', user_level = '{}' WHERE username = '{}'".format
      (max(row[1], SCORE), max(row[2], LEVEL), user)
   )
   conn.commit()

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

    print("Enter your name")
    username = input()
    cur.execute("SELECT count(*) FROM usertable WHERE username='{}'".format(username))
    conn.commit()
    if cur.fetchone()[0] == 0:
        insertname(username)
        conn.commit()
    else:
        cur.execute("SELECT * FROM usertable WHERE username = '{}'".format(username))
        data = cur.fetchone()
        print("User's max score:{}".format(data[1]))
        print("User's max level:{}".format(data[2]))

    PAUSE = False
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
                cur.close()
                conn.close()
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
                elif event.key == pygame.K_SPACE:
                    upd(username, Score, LEVEL)
                    pause = True
            if event.type == time_event:
                CD -= 1
                if CD == 0:
                    CD = 7
                    food.location.x = random.randint(0, screenrect.right // block - 1)
                    food.location.y = random.randint(0, screenrect.bottom // block - 1)
                    food_id = random.randint(0, 2)


        while PAUSE:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    cur.close()
                    conn.close()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_u:
                    pause = False
            unpause = pygame.font.SysFont("arial", 35).render('Press u to unpause', True, 'white')
            screen.blit(unpause, unpause.get_rect(center=(700 // 2, 700 // 2)))
            pygame.display.update()

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
                    cur.close()
                    conn.close()
                    sys.exit()
        pygame.display.update()

if __name__ == '__main__':
    main()