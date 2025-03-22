from turtle import Turtle, Screen

dudu = Turtle()
dudu.shape("arrow")
dudu.color("red")
dudu.pensize(5)
dudu.pencolor("red")

screen = Screen()
screen.listen()


def move_forward():
    dudu.forward(10)


def move_backward():
    dudu.backward(10)


def move_left():
    dudu.left(20)


def move_right():
    dudu.right(20)


def clear():
    dudu.clear()
    dudu.penup()
    dudu.home()
    dudu.pendown()


screen.onkey(key='w', fun=move_forward)
screen.onkey(key='s', fun=move_backward)
screen.onkey(key='a', fun=move_left)
screen.onkey(key='d', fun=move_right)
screen.onkey(key='c', fun=clear)

screen.exitonclick()
