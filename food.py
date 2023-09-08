from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("red")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)    # Create a circular object with size 10px x 10px
        self.speed("fastest")   # Set speed to fastest to make it invisible
        self.spawn()

    def spawn(self):    # Spawn food randomly within the screen
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
