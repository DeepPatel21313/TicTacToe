from tkinter import *
import random
import dimension
import configure


def next_turn(row, column):
    global player
    if buttons[row][column]["text"] == "" and check_winner() is False:
        if player == players[0]:
            buttons[row][column]["text"]=player
            if check_winner() is False:
                player = players[1]
                label.config(text=("Player " + players[1] + " 's turn"))
            elif check_winner() is True:
                label.config(text=("Player " + players[0] + " Wins! Congratulations!"))

            elif check_winner() == "Tie":
                label.config(text="It's a Tie!")
        else:
            buttons[row][column]["text"]=player
            if check_winner() is False:
                player = players[0]
                label.config(text=("Player " + players[0] + " 's turn"))
            elif check_winner() is True:
                label.config(text=("Player " + players[1] + " Wins! Congratulations!"))

            elif check_winner() == "Tie":
                label.config(text="It's a Tie!")


def check_winner():
    for row in range(3):
        if buttons[row][0]["text"] == buttons[row][1]["text"] == buttons[row][2]["text"] != "":
            buttons[row][0].config(bg="#2EE11E")
            buttons[row][1].config(bg="#2EE11E")
            buttons[row][2].config(bg="#2EE11E")
            return True
    for column in range(3):
        if buttons[0][column]["text"] == buttons[1][column]["text"] == buttons[2][column]["text"] != "":
            buttons[0][column].config(bg="#2EE11E")
            buttons[1][column].config(bg="#2EE11E")
            buttons[2][column].config(bg="#2EE11E")
            return True

    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        buttons[0][0].config(bg="#2EE11E")
        buttons[1][1].config(bg="#2EE11E")
        buttons[2][2].config(bg="#2EE11E")
        return True
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="#2EE11E")
        buttons[1][1].config(bg="#2EE11E")
        buttons[2][0].config(bg="#2EE11E")
        return True
    elif empty_spaces() is False:
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="#FAEC28")
        return "Tie"
    else:
        return False


def empty_spaces():
    spaces = 9

    for row in range(3):
        for column in range(3):
            if buttons[row][column]["text"] != "":
                spaces -= 1
    if spaces == 0:
        return False
    else:
        return True


def new_game():
    global player

    player = random.choice(players)
    label.config(text="Player " + player + " 's turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="#F6C4D3")


window = Tk()
window.title("Tic Tac Toe")

window.configure(bg="#89E4EF")
window.geometry(f'{configure.width}x{configure.height}')
window.resizable(False, False)

players = ["X", "O"]
player = random.choice(players)

buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]
           ]

top_frame = Frame(window, bg="#C9F499", width=configure.width, height=dimension.height_percent(25))
top_frame.place(x=0, y=0)

game_title = Label(top_frame, bg="#C9F499", fg="#C599F4", text="Tic Tac Toe", font=("Comic Sans MS", 50))
game_title.place(x=dimension.width_percentage(35), y=dimension.height_percent(4))

label = Label(top_frame, text="Player " + player + " 's turn", font=("Comic Sans MS", 20), bg="#C9F499", fg="#C599F4")
label.place(x=dimension.width_percentage(43), y=dimension.height_percent(18))

new_game = Button(top_frame, text="New game", bg="#E45062", fg="#50E4D1", font=("Comic Sans MS", 20),command=new_game)
new_game.place(x=dimension.width_percentage(10), y=dimension.height_percent(10))

bottom_frame = Frame(window, bg="#C9F499", width=450, height=450)
bottom_frame.place(x=dimension.width_percentage(27), y=dimension.height_percent(35))
# frame = Frame(window)
# frame.pack()
for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(bottom_frame, text="", font=('helvetica', 40), width=5, height=1,
                                      bg="#F6C4D3",
                                      command=lambda row=row, column=column: next_turn(row, column))
        buttons[row][column].grid(row=row, column=column)


window.mainloop()
