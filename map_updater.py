import pandas
from turtle import Turtle


class MapUpdate(Turtle):

    def __init__(self):
        super().__init__()
        self.data = pandas.read_csv("50_states.csv")
        self.state_obj = Turtle()
        self.state_obj.hideturtle()
        self.state_obj.penup()

    def move_state(self, coordinates, state):
        self.state_obj.hideturtle()
        self.state_obj.goto(coordinates)
        self.state_obj.write(state)

    def state_loc(self, guessed_state):
        x = int(self.data[self.data.state == guessed_state]["x"])
        y = int(self.data[self.data.state == guessed_state]["y"])
        return x, y

