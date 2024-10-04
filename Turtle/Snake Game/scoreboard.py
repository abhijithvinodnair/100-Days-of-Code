from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 17, 'normal')
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_score()
        self.hideturtle()
    def update_score(self):
        self.clear()
        self.goto(0, 270)
        self.write(f"Score: {self.score} Highscore: {self.highscore}",align=ALIGNMENT,font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.update_score()


    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"Game Over", align = ALIGNMENT, font = FONT)
    def increase_score(self):
        self.score+=1
        self.update_score()



