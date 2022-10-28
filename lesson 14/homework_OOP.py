from turtle import *
from random import random, randint, choice
from time import sleep


class Window:
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    SCREEN_WIDTH_HALF = SCREEN_WIDTH // 2
    SCREEN_HEIGHT_HALF = SCREEN_HEIGHT // 2

    def __init__(self, screen_title: str = 'Window title'):
        self.canvas = Screen()
        self.canvas.title(screen_title)
        self.canvas.setup(self.SCREEN_WIDTH, Window.SCREEN_HEIGHT)
        self.canvas.onkey(self.canvas.bye, 'Escape')
        self.canvas.listen()
        self.canvas.tracer(0)


class Sprite(Turtle):
    def __init__(self, shape_name: str):
        super().__init__(shape=shape_name)
        self.hideturtle()
        self.up()


class Figure(Sprite):
    size = 20

    def __init__(self, figure: str):
        super().__init__(figure)
        self.color(self.get_random_color_rgb())
        self.goto(self.get_random_position())
        self.showturtle()
        self.delta_x = 0
        self.delta_y = 0

    def move_ball(self, gravity: float):
        self.goto(self.xcor() + self.delta_x, self.ycor() - self.delta_y)
        self.delta_y += gravity

    @staticmethod
    def get_random_color_rgb():
        return random(), random(), random()

    @staticmethod
    def get_random_position():
        return randint(-Window.SCREEN_WIDTH_HALF, Window.SCREEN_WIDTH_HALF), randint(0, Window.SCREEN_HEIGHT_HALF)


class Game:
    __directions = (-1, 1)
    __gravity = 0.1
    __balls_qty = 0

    def __init__(self, balls_qty: int):
        Game.__balls_qty = balls_qty
        self.window = Window()
        self.balls = self.make_balls(balls_qty)

    def run(self):
        for ball in self.balls:
            ball.delta_x = 2 * choice(self.__directions)
            ball.delta_y = 2

        while True:
            for ball in self.balls:
                ball.move_ball(Game.__gravity)
                Game.check_border(ball)
            self.window.canvas.update()
            if Game.__balls_qty < 50:
                sleep(0.0001 * Game.__balls_qty)

            self.check_collision(self.balls)

    @staticmethod
    def check_collision(balls: list[Figure]):
        for i in range(len(balls)):
            for j in range(i + 1, len(balls)):
                if balls[i].distance(balls[j]) < Figure.size:
                    balls[i].delta_x, balls[j].delta_x = balls[j].delta_x, balls[i].delta_x
                    balls[i].delta_y, balls[j].delta_y = balls[j].delta_y, balls[i].delta_y

    @staticmethod
    def check_border(ball):
        y = ball.ycor()
        x = ball.xcor()

        if y < -Window.SCREEN_WIDTH_HALF:
            ball.delta_y = -ball.delta_y

        if x > Window.SCREEN_WIDTH_HALF or x < -Window.SCREEN_WIDTH_HALF:
            ball.delta_x = -ball.delta_x

    @staticmethod
    def make_balls(qty: int):
        figures = ('turtle', 'circle', 'square', 'triangle')
        return [Figure(choice(figures)) for _ in range(qty)]


if __name__ == '__main__':
    game = Game(balls_qty=40)
    game.run()




