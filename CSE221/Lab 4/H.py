#Coprime Graph
import sys
from math import gcd

N, Q = map(int, sys.stdin.readline().strip().split())
a_list = [[0] for i in range(N+1)]
c = 1

for i in range(1, N+1):
    for j in range(1, N+1):
        if gcd(i, j) == 1 and i!=j:
            a_list[i].append(j)
    c += 1

for i in range(Q):
    X, K = map(int, sys.stdin.readline().strip().split())
    if K < len(a_list[X]):
        sys.stdout.write(str(a_list[X][K]) + "\n")
    else:
        sys.stdout.write("-1\n")