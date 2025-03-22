from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.render(x_cor=x_cor, y_cor=y_cor)

    def render(self, x_cor, y_cor):
        self.shape(name='square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color('white')
        self.penup()
        self.goto(x=x_cor, y=y_cor)

    def go_up(self):
        y_cor = self.ycor() + 20
        self.goto(x=self.xcor(), y=y_cor)

    def go_down(self):
        y_cor = self.ycor() - 20
        self.goto(x=self.xcor(), y=y_cor)
