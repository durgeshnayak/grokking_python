from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor('black')
screen.title('Pong')
screen.setup(width=800, height=600)
screen.tracer(0)
screen.listen()

scoreboard = Scoreboard()

player_1 = Paddle(x_cor=350, y_cor=0)
player_2 = Paddle(x_cor=-350, y_cor=0)

ball = Ball()

screen.onkey(key="Up", fun=player_1.go_up)
screen.onkey(key="Down", fun=player_1.go_down)

screen.onkey(key="w", fun=player_2.go_up)
screen.onkey(key="s", fun=player_2.go_down)

game_on = True

while game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(player_1) < 50 and ball.xcor() > 320 or ball.distance(player_2) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()
