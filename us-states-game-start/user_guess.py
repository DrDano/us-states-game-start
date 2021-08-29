from turtle import Turtle, Screen
import pandas


class UserGuess(Turtle):

    def __init__(self):
        super().__init__()
        self.correct_guesses = []
        self.data = pandas.read_csv("50_states.csv")
        self.state_list = self.data["state"].to_list()
        self.score = 0

    def check_answer(self):
        answer_state = Screen().textinput(title="Guess the State", prompt="What's another state's name?").lower()
        for states in self.state_list:
            if answer_state == states.lower():
                self.correct_guesses.append(answer_state)
                self.score += 1
        return answer_state

    def states_to_learn(self):
        for state in self.correct_guesses:
            self.state_list.remove(state.capitalize())
        return self.state_list
