from turtle import Turtle, Screen

dudu = Turtle()
screen = Screen()


def move_forward():
    dudu.forward(10)


screen.listen()
screen.onkey(key="space", fun=move_forward)

screen.exitonclick()