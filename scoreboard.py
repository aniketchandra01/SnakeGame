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
        self.text()

    def text(self):
        self.write(f"Score:  {self.score}", move=False, align=Alignment, font=Font)

    def game_over(self):
        self.teleport(0,0)
        self.write("Game Over", move=False, align=Alignment, font=Font)

    def update_score(self):
        self.score += 1
        self.clear()
        self.text()


