from turtle import *
from random import random, randint, choice


def make_ball_settings(ball):
    ball.hideturtle()
    ball.shape('circle')
    ball.color((random(), random(), random()))
    ball.up()
    ball.goto(randint(-SCREEN_WIDTH // 2, SCREEN_WIDTH // 2),
              randint(0, 300))
    ball.showturtle()
    return ball

def check_border(ball):
    global gravity

    y = ball.ycor()
    x = ball.xcor()

    if y < -SCREEN_HEIGHT // 2:
        ball.delta_y = -ball.delta_y

    if x > SCREEN_WIDTH // 2 or x < -SCREEN_WIDTH // 2:
        ball.delta_x = -ball.delta_x


def move_ball(ball):
    ball.goto(ball.xcor() + ball.delta_x, ball.ycor() - ball.delta_y)
    ball.delta_y += gravity


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

window = Screen()
window.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
window.tracer(0)

balls = [Turtle() for _ in range(10)]
directions = [-1, 1]

for i in range(len(balls)):
    balls[i] = make_ball_settings(balls[i])
    balls[i].delta_x = 2 * choice(directions)
    balls[i].delta_y = 2

gravity = 0.1


while True:
    for ball in balls:
        window.update()
        check_border(ball)
        move_ball(ball)

    for i in range(len(balls)):
        for j in range(i+1, len(balls)):
            if balls[i].distance(balls[j]) < 20:
                balls[i].delta_x, balls[j].delta_x = balls[j].delta_x, balls[i].delta_x
                balls[i].delta_y, balls[j].delta_y = balls[j].delta_y, balls[i].delta_y

