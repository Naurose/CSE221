#The Seven Bridges of Königsberg
import sys

N, M = map(int, sys.stdin.readline().split())
u = list(map(int, sys.stdin.readline().split()))
v = list(map(int, sys.stdin.readline().split()))
degree = [0]*(N+1)

for i in range(M):
    degree[u[i]] += 1
    degree[v[i]] += 1

odd_vertices = sum(1 for i in degree if i%2 != 0)
sys.stdout.write("YES\n" if odd_vertices == 0 or odd_vertices == 2 else "NO\n")
