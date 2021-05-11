from turtle import Turtle


class Scoreboard(Turtle):


    def __init__(self):
        super().__init__()
        self.score = 0
        with open("snake_game\data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(arg = (f"Scoreboard : {self.score}") , align="center", font=("Arial", 12, "italic"))
        self.hideturtle()
        

    def update_scoreboard(self):
        self.clear()
        self.write(arg = (f"Scoreboard : {self.score} High Score: {self.high_score}") , align="center", font=("Arial", 12, "italic"))
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("snake_game\data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()
    
    def game_over(self):
        self.goto(0, 0)
        self.write(arg = "GAME OVER" , align="center", font=("Arial", 24, "normal"))
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()