from turtle import Turtle

RIGHT_UPPER_X = 350
RIGHT_UPPER_Y = 250
LEFT_LOWER_X = -350
LEFT_LOWER_Y = -250


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape(name='circle')
        self.color('white')
        self.penup()
        self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(x=new_x, y=new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
        self.move_speed = 0.1