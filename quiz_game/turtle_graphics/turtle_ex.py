import turtle as t
import random
timmy = t.Turtle()
#timmy.shape("turtle")
#timmy.color("green")
#x = 4
#while x < 10:
#    for i in range(x):
#        timmy.forward(100)
#        timmy.right(int(360/x))
#    x += 1

t.colormode(255)
timmy.shape("turtle")
#timmy.pensize(15)
#timmy.speed("fastest")
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    y = (r, g, b)
    return y
# x = [0, 90, 180, 270]
#while True:
#    timmy.color(random_color())
#    timmy.forward(30)
#    timmy.setheading(random.choice(x))
#    
#screen = Screen()
#screen.exitonclick()
angle = 0
for i in range(360):
    timmy.circle(120)
    timmy.color(random_color())
    timmy.setheading(angle)
    angle += 20