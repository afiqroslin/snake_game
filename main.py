from turtle import Screen, Turtle
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Orochi")
screen.tracer(0)  # turn off animation

snake = Snake()

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

screen.exitonclick()
