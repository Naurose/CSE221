#Beautiful Path
import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

N, M, S, D = map(int, input().split())
S -= 1
D -= 1
w = list(map(int, input().split()))
graph = defaultdict(list)
for i in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append((v))

def dijkstra(graph, S, D):
    dist = [float('inf')] * N
    dist[S] = w[S] 
    heap = [(w[S], S)]
    while heap:
        current_weight, u = heapq.heappop(heap)
        if current_weight > dist[u]:
            continue
        
        for v in graph[u]:
            cost = current_weight + w[v]
            if dist[v] > cost:
                dist[v] = cost
                heapq.heappush(heap, (cost, v))

    return dist[D] if dist[D] != float('inf') else -1

print(dijkstra(graph, S, D))