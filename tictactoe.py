from tkinter import *
import random
def next_turn(row, column):
    global player
    if buttons[row][column]['text'] == "" and not check_winner():
        buttons[row][column]['text'] = player
        if check_winner():
            winner, winning_line = check_winner()
            if winner:
                for r, c in winning_line:
                    buttons[r][c].config(bg="green")
                label.config(text=(player + " wins"))
        elif not empty_spaces():
            label.config(text=("Tie!"))
        else:
            player = players[1] if player == players[0] else players[0]
            label.config(text=(player + " turn"))

def check_winner():
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            return buttons[row][0]['text'], [(row, 0), (row, 1), (row, 2)]

    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            return buttons[0][column]['text'], [(0, column), (1, column), (2, column)]

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        return buttons[0][0]['text'], [(0, 0), (1, 1), (2, 2)]

    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        return buttons[0][2]['text'], [(0, 2), (1, 1), (2, 0)]

    return None

def empty_spaces():
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] == "":
                return True
    return False


def new_game():
    global player
    player = random.choice(players)
    label.config(text=player+" turn")
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="",bg="#F0F0F0")

window = Tk()
window.title("Tic-Tac-Toe")
players = ["x","o"]
player = random.choice(players)
buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]
label = Label(text = player + " turn",font=('consolas',40))
label.pack(side ="top")

reset_button = Button(text="restart",font=('consolas',20),command=new_game)
reset_button.pack(side="top")

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="",font=('consolas',40),width = 5, height = 2,command=lambda row=row, column=column: next_turn(row,column))
        buttons[row][column].grid(row=row,column=column)

window.mainloop()