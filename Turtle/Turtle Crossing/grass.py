from turtle import Turtle
class Grass(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.pencolor("green")
        self.width(30)
        self.goto(-1000,240)
        self.pendown()
        self.forward(2000)