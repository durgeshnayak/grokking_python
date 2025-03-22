from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color('Red')
        self.goto(x=0, y=270)
        self.hideturtle()
        self.score = 0
        self.write(arg=self.print_score(), move=False, align="center", font=('Courier', 25, 'bold'))

    def print_score(self):
        return f"Score: {self.score}/50"

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(arg=self.print_score(), move=False, align="center", font=('Courier', 25, 'bold'))


