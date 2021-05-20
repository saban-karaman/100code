from turtle import Screen, Turtle
from paddle import Paddle
from random import randint
from ball import Ball
from scoreboard import Scoreboard
import time

scoreboard = Scoreboard()
screen = Screen()
screen.bgcolor("black")
screen.setup(width = 800, height = 600)
screen.title("Pong_Game")
screen.tracer(0)

paddle_r = Paddle(350, 0)
paddle_l = Paddle(-350, 0)
ball = Ball()




screen.listen()
screen.onkey(paddle_r.go_up, "Up")
screen.onkey(paddle_r.go_down, "Down")

screen.onkey(paddle_l.go_up, "w")
screen.onkey(paddle_l.go_down, "s")

game_is_on = True


while game_is_on:
    
    time.sleep(0.1)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    if ball.distance(paddle_r) < 50 and ball.xcor()> 320 or ball.distance(paddle_l) < 50 and ball.xcor() < -320 :
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position() 
        scoreboard.r_point()





screen.exitonclick()


