from turtle import Turtle,Screen
import pandas


class UserGuess(Turtle):

    def __init__(self):
        super().__init__()
        self.correct_guesses = []
        self.data = pandas.read_csv("50_states.csv")
        self.state_list = self.data["state"].to_list()

    def check_answer(self):
        answer_state = Screen().textinput(title="Guess the State", prompt="What's another state's name?").lower()
        for states in self.state_list:
            if answer_state == states.lower():
                self.correct_guesses.append(answer_state)
                return answer_state

    def state_loc(self):
        x = self.data[self.data["x"] == self.check_answer]
        print(x)