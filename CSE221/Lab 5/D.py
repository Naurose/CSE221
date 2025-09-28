#Through the Jungle
import sys
from collections import deque, defaultdict
input = sys.stdin.readline

N, M, S, D, K = map(int, input().split())
graph = defaultdict(list)
for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)

for node in graph:
    graph[node].sort()

def BFS(source):
    dist = {i: float('inf') for i in range(1, N + 1)}
    parent = {i: -1 for i in range(1, N + 1)}
    dist[source] = 0
    parent[source] = None
    q = deque([source])

    while q is not None:
        temp = q.popleft()
        for neighbor in graph[temp]:
            if dist[neighbor] > dist[temp] + 1:
                dist[neighbor] = dist[temp] + 1
                parent[neighbor] = temp
                q.append(neighbor)

    return dist, parent

dist_1, parent_1 = BFS(S)
if dist_1[D] == float('inf'):
    print(-1)
    exit()

path_1 = []
temp = K
while temp is not None:
    path_1.append(temp)
    temp = parent_1[temp]
path_1.reverse()