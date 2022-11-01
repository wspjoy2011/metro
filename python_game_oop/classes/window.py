"""Class for make window and settings """

from turtle import *


class Window:
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    SCREEN_WIDTH_HALF = SCREEN_WIDTH // 2
    SCREEN_HEIGHT_HALF = SCREEN_HEIGHT // 2
    FONT = ("Arial", 44, 'normal')
    level = Turtle(visible=False)
    level.color('white')
    level.penup()
    level.setposition(-SCREEN_WIDTH_HALF // 2, SCREEN_HEIGHT_HALF * 1.05)
    level.write('LEVEL', font=FONT)

    def __init__(self, screen_title: str = 'Window title'):
        self.canvas = Screen()
        self.canvas.bgcolor('black')
        self.canvas.title(screen_title)
        self.canvas.setup(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        self.canvas.onkey(self.canvas.bye, 'Escape')
        self.canvas.listen()
        self.canvas.tracer(0)
        self.game_zone = Turtle()
        self.game_zone.hideturtle()
        self.game_zone.color('white')
        self.game_zone.begin_fill()
        self.game_zone.goto(-self.SCREEN_WIDTH_HALF, self.SCREEN_HEIGHT_HALF)
        self.game_zone.goto(self.SCREEN_WIDTH_HALF, self.SCREEN_HEIGHT_HALF)
        self.game_zone.goto(self.SCREEN_WIDTH_HALF, -self.SCREEN_HEIGHT_HALF)
        self.game_zone.goto(-self.SCREEN_WIDTH_HALF, -self.SCREEN_HEIGHT_HALF)
        self.game_zone.goto(-self.SCREEN_WIDTH_HALF, self.SCREEN_HEIGHT_HALF)
        self.game_zone.end_fill()
