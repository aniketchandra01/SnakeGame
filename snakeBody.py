from turtle import *


starting_location = [(0, 0), (-20, 0), (-40, 0)]

class SnakeBody:

    def __init__(self):
        self.body = []
        self.create_snake()
        self.head = self.body[0]

    def create_snake(self):
        for position in starting_location:
            snake = Turtle()
            snake.shape("square")
            snake.color("white")
            snake.speed(0)
            snake.penup()
            snake.goto(position)
            self.body.append(snake)



    def move(self):
        for piece in range(len(self.body) - 1, 0, -1):
            x = self.body[piece - 1].xcor()
            y = self.body[piece - 1].ycor()
            self.body[piece].goto(x, y)
        self.head.forward(10)

    def go_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)


    def go_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def go_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def go_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def update_snakebody(self):
        snake = Turtle()
        snake.shape("square")
        snake.color("white")
        snake.speed(0)
        snake.penup()
        snake.goto(self.body[-1].position())
        self.body.append(snake)





