from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.goto(x=0, y=270)
        self.hideturtle()
        self.score = 0
        with open(file="data.txt", mode="r") as data:
            self.high_score = int(data.read())
        self.write(arg=self.print_score(), move=False, align="center", font=('Courier', 25, 'bold'))

    def print_score(self):
        return f"Score: {self.score} High Score: {self.high_score}"

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(arg=self.print_score(), move=False, align="center", font=('Courier', 25, 'bold'))

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg="GAME OVER", move=False, align="center", font=('Courier', 25, 'bold'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(file="data.txt", mode="w") as data:
                data.write(str(self.high_score))
        self.score = 0
        self.update_score()