import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

N, M, S, T = map(int, input().split())

S-= 1
T-= 1
graph = defaultdict(list)

for i in range(M):
    u, v, w = map(int, input().split())
    u-=1
    v-=1
    graph[u].append((v, w))


def dijkstra(graph, S):
    dist = [float('inf')]*N
    dist[S] = 0
    parent = [None]*N
    heap = [(0, S)]

    while heap:
        dist_u, u = heapq.heappop(heap)
        if dist_u > dist[u]:
            continue 
        for v, w in graph[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                parent[v] = u
                heapq.heappush(heap, (dist[v], v))
    return dist

dist_s = dijkstra(graph, S)
dist_t = dijkstra(graph, T)
time, node = float('inf'), None
for i in range(N):
    if dist_s[i] != float('inf') and dist_t[i] != float('inf'):
        temp = max(dist_s[i], dist_t[i])
        if temp < time:  
            time = temp
            node = i + 1

if node == None:
    print(-1)
else:
    print(time, node)