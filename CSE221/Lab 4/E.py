#Edge Queries
import sys
N, M = map(int, sys.stdin.readline().split())
adjacency_list = {i:0 for i in range(1, N+1)}

u_list = list(map(int, sys.stdin.readline().split()))
v_list = list(map(int, sys.stdin.readline().split()))

for u, v in zip(u_list, v_list):
    adjacency_list[u] -= 1
    adjacency_list[v] += 1
sys.stdout.write(" ".join(map(str, adjacency_list.values())) + "\n")