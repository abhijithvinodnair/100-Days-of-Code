from turtle import Turtle
class Net(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0,y = 580)
        self.right(90)
        self.pencolor("gray")
        self.pensize(5)
        while self.ycor() >= -580:
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)
