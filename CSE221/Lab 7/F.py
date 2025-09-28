#Shortest Path Revisited
import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

from collections import defaultdict
import heapq
 
N, M, S, D = map(int, input().split())
S -= 1
D -= 1
 
graph = defaultdict(list)
for i in range(M):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append((v, w))
    graph[v].append((u, w))  
 
dist = [[float('inf'), float('inf')] for _ in range(N)]
dist[S][0] = 0
heap = [(0, S)]
 
while heap:
    cost, u = heapq.heappop(heap)
    for v, w in graph[u]:
        new_cost = cost + w
        if new_cost < dist[v][0]:
            dist[v][1] = dist[v][0]
            dist[v][0] = new_cost
            heapq.heappush(heap, (new_cost, v))
        elif dist[v][0] < new_cost < dist[v][1]:
            dist[v][1] = new_cost
            heapq.heappush(heap, (new_cost, v))
print(dist[D][1] if dist[D][1] != float('inf') else -1)