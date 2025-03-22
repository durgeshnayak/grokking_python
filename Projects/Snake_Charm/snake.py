from turtle import Turtle


class Snake:
    turtles = []
    STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
    SNAKE_STEP = 20
    UP = 90
    DOWN = 270
    LEFT = 180
    RIGHT = 0

    def __init__(self):
        self.create_snake()

    def create_snake(self):
        for position in self.STARTING_POSITIONS:
            self.add_segment(position=position)

    def add_segment(self, position):
        player = Turtle()
        player.color("white")
        player.shape("square")
        player.penup()
        player.goto(position)
        self.turtles.append(player)

    def extend(self):
        self.add_segment(position=self.turtles[-1].position())

    def move(self):
        for player_number in range(len(self.turtles) - 1, 0, -1):
            self.turtles[player_number].goto(x=self.turtles[player_number - 1].xcor(),
                                             y=self.turtles[player_number - 1].ycor())
        self.turtles[0].forward(self.SNAKE_STEP)

    def up(self):
        if self.turtles[0].heading() != self.DOWN:
            self.turtles[0].setheading(90)

    def down(self):
        if self.turtles[0].heading() != self.UP:
            self.turtles[0].setheading(270)

    def left(self):
        if self.turtles[0].heading() != self.RIGHT:
            self.turtles[0].setheading(180)

    def right(self):
        if self.turtles[0].heading() != self.LEFT:
            self.turtles[0].setheading(0)

    def reset(self):
        for segment in self.turtles:
            segment.hideturtle()
        self.turtles.clear()
        self.create_snake()
