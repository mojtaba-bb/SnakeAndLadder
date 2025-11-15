import os
import tkinter as tk
from tkinter import ttk
import random
from PIL import Image, ImageTk


players = [0, 0]  
move = 0


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


tiles = []
i = 0
for y in range(10):
    if (i // 10) % 2 == 0:
        for x in range(10):
            tiles.append([x, 9 - y])
            i += 1
    else:
        for x in range(10):
            tiles.append([9 - x, 9 - y])
            i += 1


snakes = {
    33: 10,
    37: 5,
    57: 19,
    92: 55,
    97:56
}

ladders = {
    7: 45,
    34: 66,
    40: 77,
    48: 91,
    62:81,
    74:96
}


main = tk.Tk()
main.title("Snakes & Ladders - Single Player")
main.config(bg="#ffffff")
main.geometry("720x670")
main.resizable(False, False)


bg_path = os.path.join(BASE_DIR, 'assets', 'images', 'bg.jpg')
if not os.path.exists(bg_path):
    raise FileNotFoundError(f"Background not found: {bg_path}")
image = Image.open(bg_path).resize((520, 520))
img = ImageTk.PhotoImage(image)

def load_pawn(name):
    p = os.path.join(BASE_DIR, 'assets', 'pawns', name)
    if not os.path.exists(p):
        raise FileNotFoundError(f"Pawn image not found: {p}")
    return Image.open(p).convert("RGBA")


redPawnPng = load_pawn('redPawn.png')
bluePawnPng = load_pawn('bluePawn.png')
pawnsPng = [redPawnPng, bluePawnPng]
for idx in range(len(pawnsPng)):
    pawnsPng[idx] = ImageTk.PhotoImage(pawnsPng[idx].resize((20, 30)))

style = ttk.Style(main)
style.theme_use("clam")
style.configure("button.TButton", background="#E4E2E2", foreground="#000", relief=tk.FLAT)
style.map("button.TButton", background=[("active", "#E4E2E2")], foreground=[("active", "#000")])

label = ttk.Label(master=main, text="Click Dice to start", anchor="center")
label.place(x=240, y=560, width=240, height=38)

c = tk.Canvas(master=main)
c.place(x=100, y=39, width=520, height=520)
c.create_image(0, 0, image=img, anchor="nw")


pawn_user = c.create_image(16, 11 + 52 * 9, image=pawnsPng[0], anchor="nw")
pawn_cpu  = c.create_image(16 + 52 * 3, 11 + 52 * 9, image=pawnsPng[1], anchor="nw")
c.itemconfig(pawn_user, state="hidden")
c.itemconfig(pawn_cpu, state="hidden")

def update_pawns():

    if players[0] > 0:
        x = 16 + 52 * tiles[players[0] - 1][0]
        y = 11 + 52 * tiles[players[0] - 1][1]
        c.itemconfig(pawn_user, state="normal")
        c.coords(pawn_user, x, y)
    else:
        c.itemconfig(pawn_user, state="hidden")

    if players[1] > 0:
        x = 16 + 52 * tiles[players[1] - 1][0]
        y = 11 + 52 * tiles[players[1] - 1][1]
        c.itemconfig(pawn_cpu, state="normal")
        c.coords(pawn_cpu, x, y)
    else:
        c.itemconfig(pawn_cpu, state="hidden")

def randomGen():
    return random.randint(1, 6)

def check_winner(player_index):

    if players[player_index] == 100:
        if player_index == 0:
            label.config(text="You win! 🎉")
        else:
            label.config(text="Computer wins! 💻")
        button.config(state="disabled")
        return True
    return False

def end_turn_actions(current_got6):

    global move

    if not current_got6:
        move += 1


    if move % 2 == 1:
        # نوبت کامپیوتر: دکمه کاربر غیرفعال بماند و کامپیوتر بعد از تاخیر کوتاه حرکت کند
        label.config(text="Computer's turn...")
        main.after(700, computer_turn)
    else:

        button.config(state="normal")
        label.config(text="Your turn. Click Dice.")
def perform_jump_and_finish(cur, dest, message, cg6):
    
    players[cur] = dest
    update_pawns()
    label.config(text=message)

    main.after(700, lambda: end_turn_actions(cg6))

def movePawn(dice):

    current = move % 2
    current_got6 = (dice == 6)


    if players[current] == 0:
        if dice == 6:
            players[current] = 1
        else:
            update_pawns()

            end_turn_actions(current_got6)
            return
    else:
        target = players[current] + dice
        if target <= 100:
            players[current] = target



    update_pawns()


    if check_winner(current):
        return


    if players[current] in snakes:
        dest = snakes[players[current]]
        label.config(text=f"Oops! Player {current+1} landed on a Snake!")

        main.after(700, lambda cur=current, d=dest, cg6=current_got6:
                   perform_jump_and_finish(cur, d, f"Player {cur+1} slides down to {d}", cg6))
        return


    if players[current] in ladders:
        dest = ladders[players[current]]
        label.config(text=f"Yay! Player {current+1} landed on a Ladder!")
        main.after(700, lambda cur=current, d=dest, cg6=current_got6:
                   perform_jump_and_finish(cur, d, f"Player {cur+1} climbs up to {d}", cg6))
        return


    end_turn_actions(current_got6)

def computer_turn():


    dice = randomGen()
    label.config(text=f"Computer rolled {dice}")
    movePawn(dice)


def button_clicked():


    button.config(state="disabled")
    dice = randomGen()
    label.config(text=f"You rolled {dice}")
    movePawn(dice)



button = ttk.Button(master=main, command=button_clicked, text="Dice", style="button.TButton")
button.place(x=240, y=600, width=240, height=38)


update_pawns()
main.mainloop()