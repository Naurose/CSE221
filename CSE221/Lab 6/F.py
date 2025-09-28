#Nearest Tour Destination
import sys
from collections import deque
input = sys.stdin.readline

N, M, S, Q = map(int, input().split())
adj = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

sources = list(map(int, input().split()))
destinations = list(map(int, input().split()))

distance = [-1]*(N+1)
queue = deque()

for source in sources:
    if distance[source] == -1:
        distance[source] = 0
        queue.append(source)

while queue:
    u = queue.popleft()
    for v in adj[u]:
        if distance[v] == -1:
            distance[v] = distance[u] + 1
            queue.append(v)

print(' '.join(str(distance[d]) for d in destinations))