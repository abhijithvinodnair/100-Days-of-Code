import random
from turtle import Turtle,Screen
is_race_on = False
screen = Screen()
screen.setup(500,400)
user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color:\n1.Red\n2.Blue\n3.Green\n4.Gray\n5.Brown\n6.Yellow").lower()

def turtle_task(name):
    name.penup()
    name.shape("turtle")
turtle_names = ['alex','benny','mathew','benny','mili','lany']
all_turtles = []
turtle_color = ['red','blue','green','gray','brown','yellow']
turtle_position = [0,-30,30,-60,50,-90]
for turtle_index in range(6):
    new_turtle = Turtle(shape ="turtle")
    turtle_task(new_turtle)
    new_turtle.color('black', turtle_color [turtle_index])
    new_turtle.goto(x = -230, y = turtle_position [turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)
        if int(turtle.xcor()) > 230:
            color = turtle.fillcolor()
            is_race_on = False
            if user_bet == color:

                print(f"Yay! The {color} turtle finished first. You have won the bet.")
            else:
                print(f"Oh No! The {color} turtle finished first. You have lost the bet.")

            break


screen.exitonclick()
