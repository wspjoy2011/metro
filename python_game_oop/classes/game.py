"""Game logic class"""
from random import choice
from time import sleep
from turtle import *

from classes.window import Window
from classes.figure import Figure
from classes.player_object import PlayerObject


class Game:
    __directions = (-1, 1)
    figure_qty = 5
    level_counter = 1
    FONT = ("Arial", 44, 'normal')

    def __init__(self):
        Game.__balls_qty = Game.figure_qty
        self.window = Window()
        self.move_detector = Screen()
        self.player = PlayerObject('turtle')

    def run(self):

        level = Turtle(visible=False)
        level.color('white')
        level.penup()
        level.setposition(Window.SCREEN_WIDTH_HALF // 2, Window.SCREEN_HEIGHT_HALF * 1.05)
        level.write(self.level_counter, font=Game.FONT)

        figures = self.make_figures(Game.figure_qty)
        for figure in figures:
            figure.delta_x = 2 * choice(self.__directions)
            figure.delta_y = 2

        while True:
            for figure in figures:
                figure.move()
                Game.check_border(figure)
            self.window.canvas.update()

            if Game.figure_qty < 50:
                sleep(0.01 * Game.figure_qty)

            self.check_collision(figures)
            self.move_detector.onkey(self.player.move_up, 'w')
            self.move_detector.onkey(self.player.move_down, 's')
            self.move_detector.listen()
            Game.game_rules(figures, self.player)

            if self.player.ycor() == Window.SCREEN_HEIGHT_HALF:
                Game.level_counter += 1
                Game.figure_qty += 1
                self.player.goto(x=0, y=-Window.SCREEN_HEIGHT_HALF * 0.9)
                for figure in figures:
                    figure.hideturtle()
                    level.clear()
                self.run()

    @staticmethod
    def check_collision(figures: list[Figure]):
        for i in range(len(figures)):
            for j in range(i + 1, len(figures)):
                if figures[i].distance(figures[j]) < Figure.size:
                    figures[i].delta_x, figures[j].delta_x = figures[j].delta_x, figures[i].delta_x

    @staticmethod
    def game_rules(figures: list[Figure], player_object: PlayerObject):
        for figure in figures:
            if figure.distance(player_object) < Figure.size:
                player_object.goto(x=0, y=-Window.SCREEN_HEIGHT_HALF * 0.9)

    @staticmethod
    def check_border(figure):
        x = figure.xcor()

        if x > Window.SCREEN_WIDTH_HALF or x < -Window.SCREEN_WIDTH_HALF:
            figure.delta_x = -figure.delta_x

    @staticmethod
    def make_figures(figures_qty: int):
        figures = ('turtle', 'circle', 'triangle')
        return [Figure(choice(figures)) for _ in range(figures_qty)]
