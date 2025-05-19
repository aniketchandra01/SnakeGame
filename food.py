from turtle import *
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.shape("circle")
        self.color("yellow")
        self.teleport(random.randint(-260,260),random.randint(-260,260))

    def collision(self):
        self.teleport(random.randint(-260,260),random.randint(-260,260))
