import pygame, random
from point import Point

global block
block = 25

class Snake():
    def __init__(self, screen):
        self.screen = screen
        self.screenrect = screen.get_rect()
        self.body = [
            Point(
                x=self.screenrect.right // block // 2,
                y=self.screenrect.bottom // block // 2,
            ),
            Point(
                x=self.screenrect.right // block // 2 + 1,
                y=self.screenrect.bottom // block // 2,
            ),
        ]

    def draw(self):
        head = self.body[0]
        pygame.draw.rect(
            self.screen,
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
                self.screen,
                (220, 0, 0),
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

        if self.body[0].x > self.screenrect.right // block:
            self.body[0].x = 0
        elif self.body[0].x < 0:
            self.body[0].x = self.screenrect.right // size
        elif self.body[0].y < 0:
            self.body[0].y = self.screenrect.right // size
        elif self.body[0].y > self.screenrect.bottom // size:
            self.body[0].y = 0

    def check_collision(self, food):
        if food.location.x != self.body[0].x:
            return False
        if food.location.y != self.body[0].y:
            return False
        return True

def draw_grid(screen):
    screenrect = screen.get_rect()
    for x in range(0, screenrect.right, block):
        pygame.draw.line(screen, 'white', start_pos=(x, 0), end_pos=(x, screenrect.bottom), width=1)
    for y in range(0, screenrect.bottom, block):
        pygame.draw.line(screen, 'white', start_pos=(0, y), end_pos=(screenrect.right, y), width=1)

class Food:
    def __init__(self, screen, x, y):
        self.location = Point(x, y)
        self.screen = screen

    def draw(self):
        pygame.draw.rect(
            self.screen,
            'green',
            pygame.Rect(
                self.location.x * block,
                self.location.y * block,
                block,
                block,
            )
        )
    def draw2(self):
        pygame.draw.rect(
            self.screen,
            'yellow',
            pygame.Rect(
                self.location.x * block,
                self.location.y * block,
                block,
                block,
            )
        )



