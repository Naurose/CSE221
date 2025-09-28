# A Football Match
import sys
from collections import deque, defaultdict
input = sys.stdin.readline

N, M = map(int, input().split())
graph = defaultdict(list)

for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def bipartite(graph):
    color = {i: -1 for i in range(1, N + 1)}
    queue = deque()
    result = 0
    for node in range(1, N+1):
        if color[node] == -1:
            zero = 0
            one = 0
            queue.append(node)
            color[node] = 1
            one += 1
            while queue:
                temp = queue.popleft()
                for i in graph[temp]:
                    if color[i] == -1:
                        if color[temp] == 1:
                            color[i] = 0
                            zero += 1
                        elif color[temp] == 0:
                            color[i] = 1
                            one += 1
                        queue.append(i)
            
            result += max(zero, one)
    
    return result
print(bipartite(graph))