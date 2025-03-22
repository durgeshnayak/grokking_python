from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Charm")
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

screen_snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.onkey(fun=screen_snake.up, key="Up")
screen.onkey(fun=screen_snake.down, key="Down")
screen.onkey(fun=screen_snake.left, key="Left")
screen.onkey(fun=screen_snake.right, key="Right")

screen.update()

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    screen_snake.move()

    if screen_snake.turtles[0].distance(food) < 15:
        food.refresh()
        screen_snake.extend()
        scoreboard.update_score()

    if screen_snake.turtles[0].xcor() > 280 or screen_snake.turtles[0].xcor() < -280 or screen_snake.turtles[0].ycor() > 280 or screen_snake.turtles[0].ycor() < -280:
        scoreboard.reset()
        screen_snake.reset()

    for segment in screen_snake.turtles[1:]:
        if screen_snake.turtles[0].distance(segment) < 10:
            scoreboard.reset()
            screen_snake.reset()


screen.exitonclick()
