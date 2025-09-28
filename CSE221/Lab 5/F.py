#Cycle Detection

import sys
from collections import defaultdict
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
graph = defaultdict(list)

for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
visited = [0]*(N+1)

def DFS(u):
    visited[u] = 1
    for v in graph[u]:
        if visited[v] == 0:
            if DFS(v):
                return True
        elif visited[v] == 1:
            return True
    visited[u] = 2
    return False

for i in range(1, N + 1):
    if visited[i] == 0:
        if DFS(i):
            print("YES")
            exit()
print("NO")