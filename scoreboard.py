from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, point):
        super().__init__()
        self.color("blue")
        self.penup()
        self.hideturtle()
        self.setposition(0, 250)
        self.write(arg=f'Score = {point}', move=True, align='center', font=("Courier", 20, "bold"))

