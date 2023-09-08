from turtle import Turtle


class Scoreboard(Turtle):
    '''
    Create scoreboard on the screen to let player keep track of their score and display game over when the snake
    collide with the wall or with itself.
    '''
    def __init__(self):
        super().__init__()
        self.point = 0
        self.color("blue")
        self.penup()
        self.goto(0, 250)   # Position the text on the center top of the screen
        self.hideturtle()       # Hide turtle so only the text are visible
        self.update_scoreboard()

    def update_scoreboard(self):    # Write 'Score' on the screen
        self.write(arg=f'Score = {self.point}', align='center', font=("Courier", 20, "bold"))

    def game_over(self):
        self.goto(0, 0)     # Display Game Over, whenever player lose the game
        self.write(arg='Game Over!', align='center', font=("Courier", 50, "bold"))

    def increase_score(self):   # Increase the score everytime the snake hit the food and update the scoreboard
        self.point += 1
        self.clear()
        self.update_scoreboard()
