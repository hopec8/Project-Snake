from turtle import Turtle

with open("data.txt", mode="r") as file:
    HIGH_SCORE = int(file.read())


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = HIGH_SCORE
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(arg=f"Score: {self.score} High Score: {self.highscore}", align="center", font=("Arial", 24, "normal"))
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.highscore}", align="center", font=("Arial", 24, "normal"))

    def reset_scoreboard(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.highscore))
        self.clear()
        self.score = 0
        self.update_scoreboard()

