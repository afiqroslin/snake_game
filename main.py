# Author : Afiq Roslin, https://github.com/afiqroslin

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600) # Set the screen size of 600x600
screen.bgcolor("black")
screen.title("Orochi")
screen.tracer(0)  # turn off animation

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.left, "Left")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()  # Refresh the graphics after all squares moved so it looks like it is one entity moving
    time.sleep(0.1)
    snake.move_snake()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.spawn()
        snake.extend()
        score.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()

    # Detect collision with tail
    for segment in snake.segment[1:]:       # Go through snake segment list by excluding the head
        if snake.head.distance(segment) < 10:   # If the head and the body distance less than 10px, end game
            game_is_on = False
            score.game_over()
            # print(snake.head.distance(segment))

screen.exitonclick()
