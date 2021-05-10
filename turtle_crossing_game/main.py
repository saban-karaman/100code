import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from random import randint
scoreboard = Scoreboard()
screen = Screen()
screen.bgcolor("white")
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player = Player()
car = CarManager()

screen.onkey(player.move, "Up")
timer = 0.1
game_is_on = True
while game_is_on:
    time.sleep(timer)
    screen.update() 
    car.create_car()
    car.move_cars()
    for i in car.all_cars:
        if player.distance(i) < 15:
            scoreboard.game_over()
            game_is_on = False
    if player.ycor() == 290:
        scoreboard.game_level()
        player.goto(0,-280)
        timer *= 0.5
        
    
    
    





screen.exitonclick()