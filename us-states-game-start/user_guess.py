from turtle import Turtle,Screen
import pandas

class UserGuess(Turtle):
    def __init__(self):
        super().__init__()
        self.correct_guesses = []
        self.data = pandas.read_csv("50_states.csv")


    def user_answer(self):
        answer_state = Screen().textinput(title="Guess the State", prompt="What's another state's name?").lower()

    def check_answer(self):

