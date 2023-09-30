import random
from turtle import Turtle
START_MOVING_DISTANCE = 5
MOVE_INCREMENT = 10

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = START_MOVING_DISTANCE

    def create_car(self):
        if random.randint(1, 5) == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.pu()
            new_car.setheading(180)
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.forward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
