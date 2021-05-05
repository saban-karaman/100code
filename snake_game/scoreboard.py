from turtle import Turtle

class Scoreboard(Turtle):


    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(arg = (f"Scoreboard : {self.score}") , align="center", font=("Arial", 12, "italic"))
        self.hideturtle()
        

    def update_scoreboard(self):
        self.write(arg = (f"Scoreboard : {self.score}") , align="center", font=("Arial", 12, "italic"))
    
    def game_over(self):
        self.goto(0, 0)
        self.write(arg = "GAME OVER" , align="center", font=("Arial", 24, "normal"))
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()