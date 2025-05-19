from turtle import *

class Boarder(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.pensize(3)
        self.create_boarder()

    def create_boarder(self):
        self.teleport(-270,270)
        self.goto(-270,-270)
        self.goto(270,-270)
        self.goto(270,270)
        self.goto(-270,270)
        self.hideturtle()