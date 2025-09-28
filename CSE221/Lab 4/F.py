'''
The King of Konigsberg

You are given an N*N chessboard and the initial position (x,y) of a King piece. 
The King can move one step in any of the 8 possible directions: 
- Up
- Down 
- Left
- Right
- Top-left diagonal
- Top-right diagonal
- Bottom-left diagonal
- Bottom-right diagonal

Moves of a King in Chess
Your task is to determine the number of valid moves the King can make in one move.
A move is valid if it remains inside the board.
'''
import sys
chess_size = int(sys.stdin.readline().strip())
x, y = map(int, sys.stdin.readline().strip().split())

k = []
for i in range(x-1, x+2):
    for j in range(y-1, y+2):
        if i > 0 and i <= chess_size and j > 0 and j <= chess_size and (i != x or j != y):
            k.append((i, j))
sys.stdout.write(str(len(k)) + "\n")
for move in k:
    sys.stdout.write(f"{move[0]} {move[1]}\n")