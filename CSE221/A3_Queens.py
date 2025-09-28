SIZE = 8
queens = [-1] * SIZE

def is_valid(row, col):
    for i in range(1, row + 1):
        if (queens[row - i] == col or
            queens[row - i] == col - i or
            queens[row - i] == col + i):
            return False
    return True

def find_position(k):
    start = queens[k] + 1
    for j in range(start, SIZE):
        if is_valid(k, j):
            return j
    return -1

def search():
    k = 0
    while 0 <= k < SIZE:
        j = find_position(k)
        if j < 0:
            queens[k] = -1
            k -= 1
        else:
            queens[k] = j
            k += 1
    return k != -1

def print_board():
    for r in range(SIZE):
        print("".join("Q" if c == queens[r] else "□" for c in range(SIZE)))

# runs immediately whether executed or imported
if search():
    print("One solution (row -> column):", queens)
    print("\nBoard:")
    print_board()
else:
    print("No solution found.")
