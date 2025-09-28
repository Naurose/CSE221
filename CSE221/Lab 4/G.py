import sys
N, M, K = map(int, sys.stdin.readline().split())
knights = []

for i in range(K):
    x, y = map(int, sys.stdin.readline().split())
    knights.append((x, y))

moves = set(knights)
flag = False

for x, y in knights:
    for i in range(x-2, x+3):        
        for j in range(y-2, y+3):    
            if 1 <= i <= N and 1 <= j <= M and (i!=x or j!=y):
                dx, dy = abs(i-x), abs(j-y)
                if dx*dy == 2 and (i, j) in moves:
                    flag = True
                    break
        if flag:
            break
    if flag:
        break

print("YES" if flag else "NO")
