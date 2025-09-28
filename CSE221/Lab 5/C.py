import sys
from collections import defaultdict, deque
input = sys.stdin.readline
N, M, S, D = map(int, input().split())
graph = defaultdict(list)

a = list(map(int, input().split()))
b = list(map(int, input().split()))
for u, v in zip(a, b):
    graph[u].append(v)
    graph[v].append(u)

for node in graph:
    graph[node].sort()

dist = {i: float('inf') for i in range(1, N + 1)}
parent = {i: -1 for i in range(1, N + 1)}
dist[S] = 0
parent[S] = None

q = deque([S])

def bfs():
    while q:
        temp = q.popleft()
        for neighbor in graph[temp]:
            if dist[neighbor] > dist[temp] + 1:
                dist[neighbor] = dist[temp] + 1
                parent[neighbor] = temp
                q.append(neighbor)

bfs() 

if dist[D] == float('inf'):
    print(-1)
else:
    path = []
    temp = D
    while temp is not None:
        path.append(temp)
        temp = parent[temp]
    print(len(path) - 1)
    print(*reversed(path))