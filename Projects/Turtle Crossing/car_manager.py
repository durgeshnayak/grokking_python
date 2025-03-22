from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
START_POSITION = 280


class CarManager:

    def __init__(self):
        self.cars = []
        # self.cleanup = []

    def create_cars(self, count):
        for _ in range(count):
            self.cars.append(self.create_car())

    def create_car(self):
        car = Turtle()
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.color(random.choice(COLORS))
        xcor = START_POSITION
        ycor = random.randint(-250, 250)
        car.penup()
        car.goto(x=xcor, y=ycor)
        car.shape("square")
        return car

    # def cleanup_cars(self, cleanup_list):
    #     for car in cleanup_list:
    #         self.cars.remove(car)

    def animate_cars(self, level):
        for car in random.choices(population=self.cars, k=int(len(self.cars) / 2)):
            if car.xcor() < -280:
                car.hideturtle()
            else:
                car.penup()
                car.setheading(180)
                car.forward(STARTING_MOVE_DISTANCE + (level * MOVE_INCREMENT))

