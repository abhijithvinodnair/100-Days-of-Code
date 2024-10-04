from turtle import Screen
from paddle import Paddle
from ball import Ball
from net import Net
from scoreboard import Scoreboard
import time
screen = Screen()
speed =0.005
screen.bgcolor("black")
screen.setup(800,600)
screen.title("Pong Game")
screen.tracer(0)
PADDLE_POSITIONS = [(350,0)]
left_paddle = Paddle(x = -350,y = 0)
right_paddle = Paddle(350,0)
ball = Ball()
net = Net()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(left_paddle.go_up, "Up")
screen.onkey(left_paddle.go_down, "Down")
screen.onkey(right_paddle.go_up, "w")
screen.onkey(right_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(speed)
    screen.update()
    ball.move()
    if ball.xcor() < -330 and ball.distance(left_paddle) < 50 or ball.xcor() > 330 and ball.distance(right_paddle) < 50:
        ball.bounce_x()
        speed *=0.9
    if ball.xcor() > 380:
        ball.reset_position()
        speed = 0.005
        scoreboard.l_point()


    if ball.xcor() < -380:
        ball.reset_position()
        speed = 0.005
        scoreboard.r_point()

screen.exitonclick()
