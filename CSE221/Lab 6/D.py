#Whats's the Diamaeter
import sys
from collections import deque, defaultdict
input = sys.stdin.readline

N = int(input())
graph = defaultdict(list)

for i in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def BFS(graph, source):
    level = defaultdict(int)
    level[source] = 0

    visited = set()
    visited.add(source)
    Q = deque([source])

    farthest = source
    max_dis = 0

    while Q:
        node = Q.popleft()
        for i in graph[node]:
            if i not in visited:
                visited.add(i)
                level[i] = level[node] + 1
                Q.append(i)
                
                if level[i] > max_dis:
                    max_dis = level[i]
                    farthest = i
    
    return farthest, max_dis

node, dis = BFS(graph, 1)
source, distance = BFS(graph, node)
print(distance)
print(node, source)