from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0


class Snake:

    def __init__(self):  # Create snake and position when the class is called by an object
        self.position = []
        self.create_snake()
        self.head = self.position[0]

    def create_snake(self):
        initial_pos = 0
        for snake_count in range(0, 3):  # Spawn 3 squares side by side to create a snake
            snake = Turtle()
            snake.shape("square")
            snake.color("white")
            snake.penup()
            snake.goto(initial_pos, 0)
            initial_pos -= 20
            self.position.append(snake)

    def move_snake(self):
        for pos in range(len(self.position) - 1, 0,
                         -1):  # When the 1st square (head) move, the last square (tail) will take second square
            # position and 2nd square will take 1st square position
            new_x = self.position[
                pos - 1].xcor()  # assign new x coordinate to each square by replacing the square in front position
            new_y = self.position[pos - 1].ycor()  # assign new y coordinate to each square
            self.position[pos].goto(new_x, new_y)  # the square will move the respective position
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
