import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from grass import Grass
from Road import Road
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
grass = Grass()
road = Road()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(player.jump,"space")
game_is_on = True
while game_is_on is True:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    #collision with cars
    for car in car_manager.all_cars:
        if car.distance(player) < 25:
            game_is_on = False
            scoreboard.game_over()
    if player.ycor() == 250:
        player.refresh()
        car_manager.refresh()
        scoreboard.point()
        car_manager.change_car_speed()

screen.exitonclick()
