import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk  # install Pillow: pip install pillow

SIZE = 8
CELL = 55

# board state: queens[r] = column index of queen in row r
queens = [-1] * SIZE


def is_valid(row, col):
    """Check if placing a queen at (row, col) is valid."""
    for i in range(1, row + 1):
        if queens[row - i] == col or \
           queens[row - i] == col - i or \
           queens[row - i] == col + i:
            return False
    return True


def find_position(k):
    """Find a valid column for row k, starting from last tried+1."""
    start = queens[k] + 1
    for j in range(start, SIZE):
        if is_valid(k, j):
            return j
    return -1


def search():
    """Backtracking search for one solution."""
    k = 0
    while k >= 0 and k < SIZE:
        j = find_position(k)
        if j < 0:
            queens[k] = -1
            k -= 1
        else:
            queens[k] = j
            k += 1
    return k != -1


# ---- Tkinter GUI ----
root = tk.Tk()
root.title("Eight Queens")

frame = ttk.Frame(root, padding=10)
frame.grid()

canvas = tk.Canvas(frame, width=SIZE * CELL, height=SIZE * CELL)
canvas.grid(row=0, column=0)

# load queen image
queen_img = Image.open("queen.png").resize((CELL - 10, CELL - 10))
queen_icon = ImageTk.PhotoImage(queen_img)

# draw chessboard squares
squares = []
for r in range(SIZE):
    row = []
    for c in range(SIZE):
        x1, y1 = c * CELL, r * CELL
        x2, y2 = x1 + CELL, y1 + CELL
        color = "white" if (r + c) % 2 == 0 else "lightgray"
        rect = canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")
        row.append(rect)
    squares.append(row)

# run the search and place queens
if search():
    for r in range(SIZE):
        c = queens[r]
        x, y = c * CELL + CELL // 2, r * CELL + CELL // 2
        canvas.create_image(x, y, image=queen_icon)

root.mainloop()
