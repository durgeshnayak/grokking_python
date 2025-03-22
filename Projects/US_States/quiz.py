import turtle
import pandas
import scoreboard

raw_data = pandas.read_csv(filepath_or_buffer="./50_states.csv")
state_names = raw_data["state"]

screen = turtle.Screen()
screen.title("U.S. States Quiz")
image = "blank_states_img.gif"
screen.addshape(image)
screen.tracer(0)
turtle.shape(image)
score_board = scoreboard.Scoreboard()
screen.update()

correct_responses = []
states_list = state_names.tolist()

while score_board.score <= 50:
    response = screen.textinput(title="U.S. States Quiz", prompt="What's another state's name?").title()
    if response == "Exit":
        break
    if response in states_list:
        correct_responses.append(response)
        state_data_row = raw_data[raw_data["state"] == response]
        state = turtle.Turtle()
        state.shape("circle")
        state.color("black")
        state.shapesize(stretch_len=0.25, stretch_wid=0.25)
        state.penup()
        state.goto(x=float(state_data_row["x"]), y=float(state_data_row["y"]))
        state.write(align="center", arg=response, font=('Courier', 13, 'bold'), move=False)
        score_board.update_score()
        score_board.print_score()
        screen.update()

remaining_states = [name for name in states_list if name not in correct_responses]

states_names = pandas.Series(data=remaining_states)
states_names.to_csv(path_or_buf="remaining_states.csv")

screen.exitonclick()


