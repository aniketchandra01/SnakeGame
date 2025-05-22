from turtle import *

Font =("Courier", 20, "bold")
Alignment = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.teleport(0, 270)
        self.hideturtle()
        self.highscore = self.HighScore()
        self.text()

    def HighScore(self):
        with open("Highscore.txt", mode="r+") as file:
            return int(file.read())

    def text(self):
        self.write(f"Score:  {self.score} Highscore : {self.highscore}", move=False, align=Alignment, font=Font)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("Highscore.txt", mode="w") as file:
                file.write(str(self.highscore))
        self.score = 0
        self.clear()
        self.text()

    def update_score(self):
        self.score += 1
        self.clear()
        self.text()


