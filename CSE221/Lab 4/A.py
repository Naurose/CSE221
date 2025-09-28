#Adjacency Matrix Representation
import sys

N, M = map(int, sys.stdin.readline().split())
adjacency_matrix = [[0]*(N) for i in range(N)]

for i in range(M):
    u, v, w = map(int, sys.stdin.readline().split())
    adjacency_matrix[u-1][v-1] = w

for j in adjacency_matrix:
    sys.stdout.write(" ".join(map(str, j)) + "\n")