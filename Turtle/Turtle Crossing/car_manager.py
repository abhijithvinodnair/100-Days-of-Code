from turtle import Turtle
import random
from types import new_class

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.hideturtle()
        self.car_speed = STARTING_MOVE_DISTANCE
    def create_cars(self):
        ran_chance = random.randint(1,6)
        if ran_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.color("black",  random.choice(COLORS))
            ran_y = random.randint(-200,200)
            new_car.goto(300,ran_y)
            self.all_cars.append(new_car)
        self.move_cars()
    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
    def change_car_speed(self):
        self.car_speed += 5

    def refresh(self):
        self.clear()
        self.create_cars()
        self.change_car_speed()