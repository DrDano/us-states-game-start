import turtle
import pandas
from user_guess import UserGuess

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
user_guess = UserGuess()

# Map object to be moved
state_obj = turtle.Turtle()
state_obj.hideturtle()
state_obj.penup()


score = 0
game_is_on = True

while game_is_on:
    user_guess.check_answer()
    correct_guess_list = user_guess.correct_guesses
    print(correct_guess_list)
    user_guess.state_loc()




screen.exitonclick()
