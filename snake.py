from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0


class Snake:

    def __init__(self):  # Create snake and position when the class is called by an object
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    # def create_snake(self):
    #     for snake_count in range(0, 3):  # Spawn 3 squares side by side to create a snake
    #         self.extend_snake()

    def create_snake(self):
        for position in STARTING_POSITION:  # Spawn 3 squares side by side to create a snake
            self.extend_snake(position)

    def extend_snake(self, position):   # Create another square and add inside the segment list
        # initial_pos = 0
        snake = Turtle()
        snake.shape("square")
        snake.color("white")
        snake.penup()
        # snake.goto(initial_pos, 0)
        # initial_pos -= 20
        snake.goto(position)
        self.segment.append(snake)

    def extend(self):
        self.extend_snake(self.segment[-1].position())      # Add another square at the tail to extend the body

    def move_snake(self):
        for pos in range(len(self.segment) - 1, 0,
                         -1):  # When the 1st square (head) move, the last square (tail) will take second square
            # position and 2nd square will take 1st square position
            new_x = self.segment[
                pos - 1].xcor()  # assign new x coordinate to each square by replacing the square in front position
            new_y = self.segment[pos - 1].ycor()  # assign new y coordinate to each square
            self.segment[pos].goto(new_x, new_y)  # the square will move the respective position
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

    def clear(self):
        self.clear()
