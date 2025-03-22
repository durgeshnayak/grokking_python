import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(title="Place your bet", prompt="Which turtle will win the race? Enter a color: ")

turtles = []


def initialize_turtles(turtle, xcor, ycor):
    turtle.penup()
    turtle.goto(x=xcor, y=ycor)
    turtles.append(turtle)


def race_complete():
    for runner in turtles:
        if round(runner.xcor(), 0) == 200:
            if runner.color()[0] == bet:
                print("You have won.")
            else:
                print(f"You lost, {runner.color()[0]} won")
            return True
    return False


def race():
    while not race_complete():
        runner = random.choice(turtles)
        runner.forward(10)


v_turtle = Turtle(shape="turtle")
v_turtle.color("violet")
initialize_turtles(v_turtle, -230, -90)

i_turtle = Turtle(shape="turtle")
i_turtle.color("indigo")
initialize_turtles(i_turtle, -230, -60)

b_turtle = Turtle(shape="turtle")
b_turtle.color("blue")
initialize_turtles(b_turtle, -230, -30)

g_turtle = Turtle(shape="turtle")
g_turtle.color("green")
initialize_turtles(g_turtle, -230, 0)

y_turtle = Turtle(shape="turtle")
y_turtle.color("yellow")
initialize_turtles(y_turtle, -230, 30)

o_turtle = Turtle(shape="turtle")
o_turtle.color("orange")
initialize_turtles(o_turtle, -230, 60)

r_turtle = Turtle(shape="turtle")
r_turtle.color("red")
initialize_turtles(r_turtle, -230, 90)

race()

screen.exitonclick()
