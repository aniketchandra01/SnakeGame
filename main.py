import time
from turtle import *
from snakeBody import SnakeBody
import food
import scoreboard
from boarder import Boarder

screen = Screen()
screen.tracer(0)
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.listen()
screen.title("Snake Game")
screen.delay(0)
boarder = Boarder()

game_is_on = True
snake = SnakeBody()
food = food.Food()
score = scoreboard.Scoreboard()


while game_is_on:


    screen.onkey(snake.go_up,"Up")
    screen.onkey(snake.go_down, "Down")
    screen.onkey(snake.go_left, "Left")
    screen.onkey(snake.go_right, "Right")

    screen.update()
    snake.move()
    time.sleep(0.1)


    if food.distance(snake.head) < 15:
        food.collision()
        score.update_score()
        snake.update_snakebody()

    if snake.head.xcor() >= 270 or snake.head.xcor() <= -270 or snake.head.ycor() <= -270 or snake.head.ycor() >= 270 :
        game_is_on = False
        score.game_over()

    for piece in snake.body:
        if piece == snake.head :
                pass
        elif snake.head.distance(piece) < 10:
            game_is_on = False
            score.game_over()

screen.mainloop()