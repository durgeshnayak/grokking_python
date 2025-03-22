import random
import turtle
from turtle import Turtle, Screen

turtle.colormode(255)
dudu = Turtle()
dudu.shape("turtle")
dudu.color("red")


def draw_square(turtle, side):
    for count in range(0, 4):
        turtle.forward(side)
        turtle.right(90)


def draw_dashed_line(turtle, step, skip, interval):
    for _ in range(interval):
        turtle.forward(step)
        turtle.penup()
        turtle.forward(skip)
        turtle.pendown()


def draw_shapes(turtle):
    colors = ["violet", "indigo", "blue", "green", "yellow3", "orange", "red", "purple"]
    index = 0
    for side in range(3, 11):
        angle = 360 / side
        turtle.color(colors[index])
        index += 1
        for _ in range(side):
            turtle.forward(100)
            turtle.right(angle)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def random_walk(turtle, speed, pen_width):
    directions = ["right", "left"]
    turtle.pensize(pen_width)
    turtle.speed(speed)
    for _ in range(100):
        turtle.color(random_color())
        turtle.forward(50)
        direction = random.choice(directions)
        if direction == "right":
            turtle.right(90)
        else:
            turtle.left(90)


def draw_spirograph(turtle, speed, pen_width, size_gap):
    turtle.pensize(pen_width)
    turtle.speed(speed)
    for _ in range(int(360 / size_gap)):
        turtle.color(random_color())
        turtle.circle(100)
        turtle.setheading(turtle.heading() + size_gap)


draw_square(dudu, 100)
draw_dashed_line(dudu, 10, 10, 5)
draw_shapes(dudu)
# random_walk(dudu, "fast", 10)
draw_spirograph(dudu, "fastest", 3, 5)

screen = Screen()

screen.exitonclick()
