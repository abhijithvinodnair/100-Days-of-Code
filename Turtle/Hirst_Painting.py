import turtle
import random
turtle.colormode(255)
color_list = [(207, 159, 82), (54, 89, 130), (146, 91, 39), (140, 26, 48), (222, 207, 104), (132, 177, 203), (158, 46, 83), (45, 55, 104), (170, 160, 39), (129, 189, 143), (83, 20, 44), (36, 43, 69), (186, 94, 106), (186, 140, 172), (84, 120, 180), (60, 39, 31), (88, 157, 92), (78, 153, 164), (195, 78, 72), (45, 74, 78), (80, 74, 44), (162, 201, 218), (58, 126, 122), (218, 176, 187), (169, 207, 170), (220, 181, 168)]
def turn():
    alex.left(angle)
    alex.penup()
    alex.forward(50)
    alex.pendown()
    alex.left(angle)
alex = turtle.Turtle()
alex.speed("fastest")
angle = 90
alex.penup()
alex.goto(-230, -220)
alex.pendown()
alex.hideturtle()
for j in range(10):
    for i in range (9):
        alex.dot(20,random.choice(color_list))
        alex.penup()
        alex.forward(50)
        alex.pendown()
    alex.dot(20,random.choice(color_list))
    turn()
    angle *= -1



screen = turtle.Screen()
screen.exitonclick()
