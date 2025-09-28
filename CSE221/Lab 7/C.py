#Minimize the danger
import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

N, M = map(int, input().split())
graph = defaultdict(list)

for i in range(M):
    u, v, w = map(int, input().split())
    u-=1
    v-=1
    graph[u].append((v, w))
    graph[v].append((u, w))

def minimize_danger(graph, start):
    danger = [float('inf')]*N
    danger[start] = 0
    heap = [(0, start)] 

    while heap:
        current_danger, u = heapq.heappop(heap)
        if current_danger > danger[u]:
            continue

        for v, w in graph[u]:
            max_danger = max(current_danger, w) 
            if max_danger < danger[v]:
                danger[v] = max_danger
                heapq.heappush(heap, (danger[v], v))
    return danger

danger = minimize_danger(graph, 0)
print(' '.join(str(D if D != float('inf') else -1) for D in danger))
