"""Base player object class"""
from random import random

from classes.sprite import Sprite
from classes.window import Window


class PlayerObject(Sprite):
    size = 30

    def __init__(self, figure):
        super().__init__(figure)
        self.color(self.get_random_color())
        self.goto(x=0, y=-Window.SCREEN_HEIGHT_HALF * 0.9)
        self.showturtle()
        self.x = 0
        self.y = 0
        self.delta_y = 0
        self.setheading(90)

    def move_up(self):
        self.sety(self.ycor() + 10)

    def move_down(self):
        self.sety(self.ycor() - 10)

    @staticmethod
    def get_random_color():
        return random(), random(), random()
