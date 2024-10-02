import turtle

alex = turtle.Turtle()
screen = turtle.Screen()

def move_forward():
    alex.forward(10)
def move_backward():
    alex.back(10)
def turn_clockwise():
    alex.right(10)
def turn_counterclockwise():
    alex.left(10)
def clearscreen():
    alex.clear()
    alex.penup()
    alex.home()
    alex.pendown()
screen.listen()
screen.onkey(key = "w", fun = move_forward)
screen.onkey(key = "s", fun = move_backward)
screen.onkey(key = "d", fun = turn_clockwise)
screen.onkey(key = "a", fun = turn_counterclockwise)
screen.onkey(key = "c", fun = clearscreen)
screen.exitonclick()
