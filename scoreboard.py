from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.scoreboard = Turtle()
        self.scoreboard.penup()
        self.scoreboard.hideturtle()
        self.scoreboard.goto(0, 300)

    def update_score(self, score):
        self.scoreboard.clear()
        self.scoreboard.write(f"Score: {score}", font=("Arial", 24, "normal"))
