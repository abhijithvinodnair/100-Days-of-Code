import turtle
from turtle import Turtle, Screen
import random
alex = Turtle()
turtle.colormode(255)
# angles = [0,90,180,270]
alex.speed("fastest")
def randomcolor():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    rgb = (r,g,b)
    return rgb

def tiltcircle(angle):
    for _ in range(int(360 / angle)):
        alex.color(randomcolor())
        alex.circle(100)
        alex.setheading(alex.heading() + angle)


tiltcircle(5)

screen = turtle.Screen()
screen.exitonclick()
