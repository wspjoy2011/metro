"""Base figures class"""


from random import random, randint

from classes.sprite import Sprite
from classes.window import Window


class Figure(Sprite):
    size = 20

    def __init__(self, figure: str):
        super().__init__(figure)
        self.color(self.get_random_color())
        self.goto(self.get_start_coord())
        self.showturtle()
        self.x = 0
        self.y = 0
        self.delta_x = 0

    def move(self):
        self.x = self.xcor()
        self.y = self.ycor()
        self.goto(self.x + self.delta_x, self.y)

    @staticmethod
    def get_random_color():
        return random(), random(), random()

    @staticmethod
    def get_start_coord():
        return randint(-Window.SCREEN_WIDTH_HALF, Window.SCREEN_WIDTH_HALF), \
               randint(-Window.SCREEN_HEIGHT_HALF * 0.7, Window.SCREEN_HEIGHT_HALF)
