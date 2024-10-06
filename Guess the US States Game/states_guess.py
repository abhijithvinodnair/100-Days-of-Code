import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
not_guessed_x = []
not_guessed_y = []
screen.addshape(image)
turtle.shape(image)
correct_guesses = 0
game_is_on = True
answer_x = 0
answer_y = 0
import pandas
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
not_guessed_states = all_states
guessed_states = []
while game_is_on:
    while len(guessed_states) < 50:
        answer_state = screen.textinput(title=f"({correct_guesses}/50 found)", prompt="Enter the name of a U.S. state")
        answer_state_title = str(answer_state).title()
        if answer_state_title == "Exit":
            for states in guessed_states:
                not_guessed_states.remove(states)
            new_data = pandas.DataFrame(not_guessed_states)
            new_data.to_csv("states_to_learn.csv")

            game_is_on = False
            break

        print(answer_state_title)
        if answer_state_title in guessed_states:
            continue
        if answer_state_title in all_states:
            correct_guesses += 1
            guessed_states.append(answer_state_title)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = data[data.state == answer_state_title]
            t.goto(state_data.x.item(), state_data.y.item())
            t.write(state_data.state.item())
    if correct_guesses == 50:
        play_again = screen.textinput(title = "Well done!", prompt = "Wow! You named all the U.S states. Do you want to play again?(Yes/No)").lower()
        if play_again == "yes":
            correct_guesses = 0
            guessed_states = []
        else:
            game_is_on = False

