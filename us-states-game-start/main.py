import turtle 
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape("us-states-game-start/blank_states_img.gif")
turtle.shape("us-states-game-start/blank_states_img.gif")


states = pandas.read_csv("us-states-game-start/50_states.csv")
state_dict = states.to_dict()
state_list = states.state.to_list()
guessed = []


while len(guessed) < 50:
    answer_state = screen.textinput(title=f"{len(guessed)}/50 States Correct", prompt="What's the another state?").title()
    
    if answer_state == "Exit":
        missing_states = []
        for state in state_list:
            if state not in guessed:
                missing_states.append(state) 
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break 
    for i in state_dict["state"].keys():
        if state_dict["state"][i] == answer_state:
            guessed.append(answer_state)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            t.goto(state_dict["x"][i], state_dict["y"][i])
            t.write(state_dict["state"][i])





