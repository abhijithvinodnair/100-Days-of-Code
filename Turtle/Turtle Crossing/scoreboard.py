from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("crimson")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_level()

    def update_level(self):
        self.clear()
        self.goto(-200, 270)
        self.write(f"Level {self.level}", align=ALIGNMENT, font=FONT)
    def point(self):
        self.level+=1
        self.update_level()

    def game_over(self):
        self.penup()
        self.color ("Black")
        self.clear()
        self.goto(0, 270)
        self.write(f"Game over. Total Score: {self.level}", align = ALIGNMENT, font = FONT,)

