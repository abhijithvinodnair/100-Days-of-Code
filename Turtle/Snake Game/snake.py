from turtle import Turtle
import random
STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
COLORS = ["OliveDrab3","OliveDrab4","PaleGreen3","PaleGreen4","SpringGreen3","SpringGreen4","SeaGreen3","SeaGreen4","Green3","Green4","YellowGreen","Aquamarine4","DarkSeaGreen4","DarkSlateGrey","chartreuse4","DarkOliveGreen4","CadetBlue4","CadetBlue"]
class Snake:
    def __init__(self):
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]
        self.head.shape("turtle")
        self.head.color("Red3")

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_snake_body(position)

    def add_snake_body(self,position):
        snake = Turtle("square")
        snake.penup()
        snake.color(random.choice(COLORS))
        snake.goto(position)
        self.snakes.append(snake)
    def reset(self):
        for segment in self.snakes:
            segment.goto(2000,2000)
        self.snakes.clear()
        self.create_snake()
        self.head = self.snakes[0]
        self.head.shape("turtle")
        self.head.color("Red3")

    def extend(self):
        self.add_snake_body(self.snakes[-1].position())


    def move(self):
        for segment in range(len(self.snakes) - 1, 0,-1):  # Adding start, stop and step (for loop) - no attributes to be specified for range in python
            new_x = self.snakes[segment - 1].xcor()
            new_y = self.snakes[segment - 1].ycor()
            self.snakes[segment].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)





