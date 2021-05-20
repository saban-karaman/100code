from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Whicg turtle will win the race? Enter a color:  ")
colors =["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-100, -60, -20, 20, 60, 100]
all_turtles = []
is_race_on = True

for turtle_index in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(x=-230, y=y_position[turtle_index])
    all_turtles.append(tim)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:   
        if turtle.xcor() > 230:
            is_race_on = False
            win_color = turtle.pencolor()
            if win_color == user_bet:
                print(f"You've won! The {win_color} turtle is the winner")
            else:
                print(f"You've lost! The {win_color} turtle is the winner")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)



#    def move_forwards():
#        tim.setheading(0)
#        tim.forward(30)
#        
#    def move_backward():
#        tim.setheading(180)
#        tim.forward(30)
#    def move_up():
#        tim.setheading(90)
#        tim.forward(30)
#    def move_down():
#        tim.setheading(270)
#        tim.forward(30)
#    def clear():
#        tim.clear()
#        tim.penup()
#        tim.home()
#        tim.pendown()
#    screen.listen()
#    screen.onkey(key="d", fun=move_forwards)
#    screen.onkey(key="a", fun=move_backward)
#    screen.onkey(key= "w",fun=move_up)
#    screen.onkey(key="s", fun=move_down)
#    screen.onkey(key="c", fun=clear)
screen.exitonclick()
