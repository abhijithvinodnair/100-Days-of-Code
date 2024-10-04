from turtle import Turtle   
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 250


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.shape("turtle")
        self.color("green","brown")

    def jump(self):
        self.forward(MOVE_DISTANCE)

    def refresh(self):
        self.clear()
        self.goto(STARTING_POSITION)
    
