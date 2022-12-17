import turtle
import pandas

scr = turtle.Screen()
timmy = turtle.Turtle()
scr.title("U.S States Game")

scr.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")
states = pandas.read_csv("50_states.csv")
rem_states = states.state.to_list()
guessed_states = []
while len(guessed_states)<50:
    answer = scr.textinput(title=f"{len(guessed_states)}/50 states correct",prompt="what's another state's name")
    if answer == "exit":
        break
    if len(states[states["state"] == answer.title()])!=0:
        guessed_states.append(answer)
        rem_states.remove(answer.title())
        answer_state = states[states["state"] == answer.title()]
        row_no = answer_state.index[0]
        answer_dict = answer_state.to_dict()
        x=answer_dict["x"][row_no]
        y=answer_dict["y"][row_no]
        timmy.hideturtle()
        timmy.penup()
        timmy.goto(x,y)
        timmy.write(answer)
#create states to learn.csv
if len(guessed_states)<50:
    new_data = pandas.DataFrame(rem_states)
    new_data.to_csv("states_to_learn.csv")

scr.exitonclick()


