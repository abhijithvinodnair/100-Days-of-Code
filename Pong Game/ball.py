from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("coral")
        self.speed("fastest")
        self.x_move = 1
        self.y_move = 1
    #     self.refresh()
    #
    # def refresh(self):
    #     random_x = random.randint(-280, 280)
    #     random_y = random.randint(-280, 280)
    #     self.goto(random_x, random_y)

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)
        #collision with upper and lower walls
        if self.ycor() == -280 or self.ycor() == 280:
            self.bounce_y()

        #collision with paddle
    def bounce_y(self):
        self.y_move *=  -1

    def bounce_x(self):
        self.x_move *= -1
    def reset_position(self):
        self.goto(0,0)
        self.bounce_x()