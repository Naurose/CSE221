#Shortest Path
import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

N, M, S, D = map(int, input().split())
S-=1
D-=1

L1 = list(map(int, input().split()))
L2 = list(map(int, input().split()))
L3 = list(map(int, input().split()))

L1 = [x-1 for x in L1]
L2 = [x-1 for x in L2]

graph = defaultdict(list)
for i in range(M):
    graph[L1[i]].append((L2[i], L3[i]))

def dijkstra(graph, S, D):
    distance = [float('inf')] * N
    distance[S] = 0
    parent = [None] * N
    heap = [(0, S)]

    while heap:
        dist_u, u = heapq.heappop(heap)
        if dist_u > distance[u]:
            continue
        for v, w in graph[u]:
            if distance[u] + w < distance[v]:
                distance[v] = distance[u] + w
                parent[v] = u
                heapq.heappush(heap, (distance[v], v))
    
    if distance[D] == float('inf'):
        return -1, []
    path = []
    temp = D
    while temp is not None:
        path.append(temp + 1)
        temp = parent[temp]
    path.reverse()
    return distance[D], path

distance, path = dijkstra(graph, S, D)
print(distance if distance != -1 else -1)
if len(path) != 0:
    print(' '.join(map(str, path)))