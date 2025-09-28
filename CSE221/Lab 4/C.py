#Graph Metamorphosis
import sys
N = int(sys.stdin.readline().strip())
adjacency_matrix = [[0]*N for i in range(N)]

for i in range(N):
    a_list = list(map(int, sys.stdin.readline().strip().split()))
    for j in range(a_list[0]):
        adjacency_matrix[i][a_list[j+1]] = 1

for row in adjacency_matrix:
    sys.stdout.write(" ".join(map(str, row)) + "\n") 
