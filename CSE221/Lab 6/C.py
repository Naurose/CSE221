#The knight of Konigsberg
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
x1, y1, x2, y2 = map(int, input().split())

moves =[(2, 1), (2, -1), (-2, 1), (-2, -1),
        (1, 2), (1, -2), (-1, 2), (-1, -2)]

dis = [[-1] * (N+1) for i in range(N+1)]
dis [x1] [y1] = 0
Q = deque([(x1, y1)])

while Q:
    x, y = Q.popleft()
    if x == x2 and y == y2:
        print(dis [x] [y])
        break 
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 1 <= nx <= N and 1 <= ny <= N and dis [nx] [ny] == -1:
            dis [nx] [ny] = dis [x] [y] + 1
            Q.append((nx, ny))

if dis [x2] [y2] == -1:
    print(-1)