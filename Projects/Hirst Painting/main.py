import colorgram
import turtle
import random

colors = colorgram.extract('painting.jpg', 100)

colors_list = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb = (r, g, b)
    colors_list.append(rgb)

dudu = turtle.Turtle()
turtle.colormode(255)
dudu.shape("arrow")


def draw_painting():
    y = -200.00
    dudu.penup()
    dudu.hideturtle()
    for row in range(10):
        dudu.goto(-200.00, y)
        dudu.pendown()
        for column in range(10):
            dot_color = random.choice(colors_list)
            dudu.dot(20, dot_color)
            dudu.penup()
            dudu.fd(50.00)
            dudu.pendown()
            y += 5.00
        dudu.penup()


draw_painting()

screen = turtle.Screen()
screen.exitonclick()
