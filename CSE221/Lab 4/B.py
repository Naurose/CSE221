#Adjacency List Representation
import sys

N, M = map(int, sys.stdin.readline().split())
adjacency_list = [[] for i in range(N+1)]

u_list = list(map(int, sys.stdin.readline().split()))
v_list = list(map(int, sys.stdin.readline().split()))
w_list = list(map(int, sys.stdin.readline().split()))

for u, v, w in zip(u_list, v_list, w_list):
    adjacency_list[u].append((v, w))

for key in range(1, N+1):
    if adjacency_list[key]:
        sys.stdout.write(f"{key}: ")
        sys.stdout.write(" ".join(f"({v}, {w})" for v, w in adjacency_list[key]) + "\n")
    else:
        sys.stdout.write(f"{key}:\n")