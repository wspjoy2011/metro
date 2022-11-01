"""Base game sprite"""

from turtle import Turtle


class Sprite(Turtle):
    def __init__(self, shape_name: str):
        super().__init__(shape=shape_name)
        self.hideturtle()
        self.up()
