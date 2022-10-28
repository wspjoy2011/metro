# Created by Agamdeep Singh / CodeWithAgam
# Youtube: CodeWithAgam
# Github: CodeWithAgam
# Instagram: @coderagam001 / @codewithagam
# Twitter: @CoderAgam001
# Linkdin: Agamdeep Singh

from turtle import Turtle, Screen, turtles
from random import randint

# Setting up the screen
s = Screen()
s.setup(500, 500)
s.title("Turtle Racing Game")
s.setworldcoordinates(-250, -250, 250, 250)

# Prompting the user to bet on a turtle to win
game_on = False
choice = s.textinput("Who Will Win?", "Which Turtle will Win. Enter the color: ")

colors = ["red", "yellow", "orange", "blue", "green", "purple"]
ypos = [-100, -60, -20, 20, 60, 100]
turtles = []

# Creating 6 Turtle Objects
for i in range(6):
    t = Turtle("turtle")
    t.color(colors[i])
    t.penup()
    t.goto(-230, ypos[i])
    turtles.append(t)

if choice:
    game_on = True

while game_on:
    for i in turtles:
        if i.xcor() > 230:
            game_on = False
            winner = i.pencolor()
            if winner != choice:
                print(f"You Lose! {i.pencolor().title()} Won the game!")
            elif winner == choice:
                print("You Won!")

        i.forward(randint(1, 10))

s.exitonclick()