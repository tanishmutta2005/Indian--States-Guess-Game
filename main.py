import turtle
import pandas

map_img = "map1.gif"
screen = turtle.Screen()
screen.addshape(map_img)
turtle.shape(map_img)


# def get_coor_on_click(x, y):
#     print(x, y)
# screen.onscreenclick(get_coor_on_click)

csv_file = "states.csv"
data = pandas.read_csv(csv_file)
# print(data.to_csv())
all_states = data.State.to_list()

guessed_states = []

while len(guessed_states) < 30:
    answer = screen.textinput(title=f"Guess State {len(guessed_states)}/30", prompt="Enter the state name: ").title()
    if answer.lower() == "exit":
        break
    if answer in all_states:
        if answer not in guessed_states:
            guessed_states.append(answer)
            t = turtle.Turtle()
            t.penup()
            t.hideturtle()
            state_data = data[data.State == answer]
            t.goto(state_data.x_coor.item(), state_data.y_coor.item())
            t.write(answer)

# is_on = True
# while is_on:
#     state_name = screen.textinput(title="enter", prompt="Enter the state: ")
#     if state_name.lower() != 'exit':
#         with open("states.csv", mode='a') as states:
#             # screen.onscreenclick(get_coor_on_click)
#             states.write(f"{state_name}\n")
#     else:
#         break
screen.mainloop()
