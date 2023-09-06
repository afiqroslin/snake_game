from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.point = 0
        self.color("blue")
        self.penup()
        self.goto(0, 250)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg=f'Score = {self.point}', align='center', font=("Courier", 20, "bold"))

    def game_over(self):
        self.goto(0, 0)
        self.write(arg='Game Over!', align='center', font=("Courier", 50, "bold"))

    def increase_score(self):
        self.point += 1
        self.clear()
        self.update_scoreboard()
