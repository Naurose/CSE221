#Advising
import sys
from collections import deque, defaultdict
input = sys.stdin.readline

N, M = map(int, input().split())
graph = defaultdict(list)
degree = defaultdict(int)

for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    if u not in degree:
        degree[u] = 0

def topological_sort(graph):
    for i in graph.values():
        for j in i:
            degree[j] += 1
    
    queue = deque()
    for i in range(1, N + 1):
        if degree[i] == 0:
            queue.append(i)
    path = []
    while queue:
        node = queue.popleft()
        path.append(node)
        for i in graph[node]:
            degree[i] -= 1
            if degree[i] == 0:
                queue.append(i)
    if len(path) != N:
        return [-1]
    else:
        return path

print(*topological_sort(graph))