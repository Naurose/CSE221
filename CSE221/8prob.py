import tkinter as tk

SIZE = 8
CELL = 60  # pixel size of each square
solutions = []


def is_valid(queens, row, col):
    """Check if a queen can be placed at (row, col)."""
    for r in range(row):
        c = queens[r]
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True


def solve(queens=None, row=0):
    """Backtracking search for all solutions."""
    if queens is None:
        queens = [-1] * SIZE
    if row == SIZE:
        solutions.append(queens.copy())
        return
    for col in range(SIZE):
        if is_valid(queens, row, col):
            queens[row] = col
            solve(queens, row + 1)
            queens[row] = -1


# --- GUI ---
class QueensGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("8 Queens Solutions")
        self.canvas = tk.Canvas(root, width=SIZE * CELL, height=SIZE * CELL)
        self.canvas.pack()

        self.status = tk.Label(root, text="", font=("Arial", 12))
        self.status.pack(pady=5)

        btn_frame = tk.Frame(root)
        btn_frame.pack()
        tk.Button(btn_frame, text="Previous", command=self.prev_solution).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Next", command=self.next_solution).grid(row=0, column=1, padx=5)

        self.index = 0
        self.draw_solution()

    def draw_solution(self):
        self.canvas.delete("all")
        sol = solutions[self.index]

        # draw chessboard
        for r in range(SIZE):
            for c in range(SIZE):
                x1, y1 = c * CELL, r * CELL
                x2, y2 = x1 + CELL, y1 + CELL
                color = "white" if (r + c) % 2 == 0 else "black"
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="grey")

        # draw queens
        for r, c in enumerate(sol):
            x, y = c * CELL + CELL // 2, r * CELL + CELL // 2
            self.canvas.create_text(x, y, text="♛", font=("Arial", CELL // 2), fill="grey")

        self.status.config(text=f"Solution {self.index + 1} of {len(solutions)}")

    def next_solution(self):
        self.index = (self.index + 1) % len(solutions)
        self.draw_solution()

    def prev_solution(self):
        self.index = (self.index - 1) % len(solutions)
        self.draw_solution()


# Run solver first
solve()

# Launch GUI
root = tk.Tk()
app = QueensGUI(root)
root.mainloop()
