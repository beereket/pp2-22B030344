import pygame
from math import *
import math

class Pen():
    def __init__(self, width, color, screen, *args, **kwargs):
        self.points = []  # [(x1, y1), (x2, y2)]
        self.width = width
        self.color = color
        self.screen = screen
    def draw(self):
        for idx, point in enumerate(self.points[:-1]):
            pygame.draw.line(
                self.screen,
                self.color,
                start_pos=point,  # self.points[idx]
                end_pos=self.points[idx + 1],
                width=self.width
            )

    def handle(self, mouse_pos):
        self.points.append(mouse_pos)

def FindVerticesOfEquilateralTriangle(center, vertex):
    x0, y0 = center
    x, y = vertex

    # Calculate the angle between the center and vertex
    theta1 = math.atan2(y - y0, x - x0)

    # Calculate the length of r using the formula we derived earlier
    r = math.sqrt((x - x0) ** 2 + (y - y0) ** 2) * 2 / math.sqrt(3)

    # Calculate the coordinates of the other two vertices using the polar coordinate formula
    # with angles of theta1 + 120 degrees and theta1 - 120 degrees
    x1 = x0 + r * math.cos(theta1 + math.radians(120))
    y1 = y0 + r * math.sin(theta1 + math.radians(120))
    x2 = x0 + r * math.cos(theta1 - math.radians(120))
    y2 = y0 + r * math.sin(theta1 - math.radians(120))

    # Return the coordinates of all three vertices
    return [(x, y), (x1, y1), (x2, y2)]

class Circle():
    def __init__(self, color, screen, start_pos):
        self.color = color
        self.start_pos = start_pos
        self.end_pos = start_pos
        self.screen = screen

    def draw(self):
        circle_center = self.start_pos
        Radius = (sqrt((self.end_pos[0] - self.start_pos[0])**2 + (self.end_pos[1] - self.start_pos[1])**2))

        pygame.draw.circle(
            self.screen,
            self.color,
            (self.start_pos[0], self.start_pos[1]),
            Radius,
            width = 5
        )
    def handle(self, mouse_pos):
        self.end_pos = mouse_pos

class RightTriangle():
    def __init__(self, color, screen, start_pos):
        self.start_pos = start_pos
        self.end_pos = start_pos
        self.color = color
        self.screen = screen

    def draw(self):
        x = self.start_pos[0]
        y = self.start_pos[1]

        x1 = self.end_pos[0]
        y1 = self.end_pos[1]
        pygame.draw.polygon(
            self.screen,
            self.color,
            ((x, y), (x1, y), (x1, y1)),
            width=5
        )

    def handle(self, mouse_pos):
        self.end_pos = mouse_pos

class Rectangle():
    def __init__(self, color,screen, start_pos):
        self.start_pos = start_pos
        self.end_pos = start_pos
        self.color = color
        self.screen = screen

    def draw(self):
        start_pos_x = min(self.start_pos[0], self.end_pos[0])
        start_pos_y = min(self.start_pos[1], self.end_pos[1])

        end_pos_x = max(self.start_pos[0], self.end_pos[0])
        end_pos_y = max(self.start_pos[1], self.end_pos[1])

        pygame.draw.rect(
            self.screen,
            self.color,
            (
                start_pos_x,
                start_pos_y,
                end_pos_x - start_pos_x,
                end_pos_y - start_pos_y,
            ),
            width=5,
        )

    def handle(self, mouse_pos):
        self.end_pos = mouse_pos

class EquilateralTriangle():
    def __init__(self, color, screen, start_pos):
        self.screen = screen
        self.color = color
        self.start_pos = start_pos
        self.end_pos = start_pos

    def draw(self):
        Distance = (sqrt((self.end_pos[1] - self.start_pos[1]) ** 2 + (self.end_pos[0] - self.start_pos[0]) ** 2))
        a = Distance * sqrt(3)
        height = sqrt(3) * a / 2

        x = self.start_pos[0]
        y = self.start_pos[1]

        pygame.draw.polygon(
            self.screen,
            self.color,
            (FindVerticesOfEquilateralTriangle((x, y), (self.end_pos[0], self.end_pos[1]))),
            width = 5
        )

    def handle(self, mouse_pos):
        self.end_pos = mouse_pos

class Square():
    def __init__(self, color, screen, start_pos):
        self.start_pos = start_pos
        self.end_pos = start_pos
        self.color = color
        self.screen = screen

    def draw(self):
        Distance = (sqrt((self.end_pos[1] - self.start_pos[1]) ** 2 + (self.end_pos[0] - self.start_pos[0]) ** 2))
        a = Distance * sqrt(2)

        start_pos_x = self.start_pos[0] - (a/2)
        start_pos_y = self.start_pos[1] - (a/2)

        pygame.draw.rect(
            self.screen,
            self.color,
            (start_pos_x,
            start_pos_y,
            int(a),
            int(a)),
            width = 5
        )

    def handle(self, mouse_pos):
        self.end_pos = mouse_pos

class Rhombus():

    def __init__(self, color, screen, start_pos):
        self.start_pos = start_pos
        self.end_pos = start_pos
        self.color = color
        self.screen = screen

    def draw(self):
        Distance = (sqrt((self.end_pos[1] - self.start_pos[1]) ** 2 + (self.end_pos[0] - self.start_pos[0]) ** 2))
        start_pos_x = min(self.start_pos[0], self.end_pos[0])
        start_pos_y = min(self.start_pos[1], self.end_pos[1])

        end_pos_x = max(self.start_pos[0], self.end_pos[0])
        end_pos_y = max(self.start_pos[1], self.end_pos[1])

        a = end_pos_x - start_pos_x
        b = end_pos_y - start_pos_y

        pygame.draw.polygon(
            self.screen,
            self.color,
            ((start_pos_x, start_pos_y + b/2), (start_pos_x + a/2, start_pos_y), (start_pos_x + a, start_pos_y + b/2), (start_pos_x + a/2, start_pos_y + b)),
            width= 5
        )

    def handle(self, mouse_pos):
        self.end_pos = mouse_pos
