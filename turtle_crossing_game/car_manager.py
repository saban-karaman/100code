from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
# NEW_Y = randint(-280, 281)

class CarManager(Turtle):



    def __init__(self):
        self.all_cars = []



    def create_car(self): 
        new_chance = randint(1,6)   
        if new_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(1, 2)
            new_car.color(choice(COLORS))
            new_car.penup()
            random_y = randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)
 

    def move_cars(self):
        for i in self.all_cars:
            i.backward(STARTING_MOVE_DISTANCE)
          

        
