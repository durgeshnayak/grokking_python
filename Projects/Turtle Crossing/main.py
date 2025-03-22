import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
car_manager.create_cars(count=1)

screen.listen()
screen.onkey(key="Up", fun=player.move)

scoreboard = Scoreboard()

game_level = 0
game_is_on = True
loop_count = 0

while game_is_on:
    time.sleep(0.1)
    if loop_count % 10 == 0:
        car_manager.create_cars(count=1)
    car_manager.animate_cars(game_level)
    screen.update()
    loop_count += 1

    for car in car_manager.cars:
        if car.isvisible():
            if player.distance(car) < 15:
                game_is_on = False
                scoreboard.game_over()

    if player.ycor() > 250:
        player.reset_player()
        scoreboard.next_level()
        game_level += 1


screen.exitonclick()
