import turtle
import pandas
from user_guess import UserGuess
import map_updater
import scoreboard

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
user_guess = UserGuess()
map_update = map_updater.MapUpdate()
score_update = scoreboard.Scoreboard()

game_is_on = True
while game_is_on:
    user_guess.check_answer()
    correct_guess_list = user_guess.correct_guesses
    correct_guess = correct_guess_list[-1].capitalize()
    state_loc = map_update.state_loc(guessed_state=correct_guess)
    map_update.move_state(state=correct_guess, coordinates=state_loc)
    score_update.update_score(score=user_guess.score)


screen.exitonclick()
