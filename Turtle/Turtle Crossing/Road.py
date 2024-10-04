from turtle import Turtle
class Road(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.pencolor("gray")
        self.width(450)
        self.goto(-800,0)
        self.pendown()
        self.forward(1600)