#Parity Edge
import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

N, M = map(int, input().split())

u = list(map(int, input().split()))
v = list(map(int, input().split()))
w = list(map(int, input().split()))

graph = defaultdict(list)
for i in range(M):
    graph[u[i] - 1].append((v[i]-1, w[i]))
    
heap = []
dist = [[float('inf'), float('inf')] for _ in range(N)]

for t, weight in graph[0]:
    parity = weight%2
    dist[t][parity] = weight
    heapq.heappush(heap, (weight, t, parity)) 

while heap:
    d, u, last_parity = heapq.heappop(heap)
    if d > dist[u][last_parity]:
        continue

    for v, w in graph[u]:
        p = w%2
        if p != last_parity:
            if dist[v][p] > d + w:
                dist[v][p] = d + w
                heapq.heappush(heap, (dist[v][p], v, p))
result = min(dist[N-1])
print(result if result != float('inf') else -1)
