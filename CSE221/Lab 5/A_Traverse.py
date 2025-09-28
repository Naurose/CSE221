# import sys
# from collections import deque
# from collections import defaultdict

# N, M = map(int, sys.stdin.readline().split())
# graph = defaultdict(list)

# for i in range(M):
#     u, v = map(int, sys.stdin.readline().split())
#     graph[u].append(v)
#     graph[v].append(u)

# def BFS(graph, source):
#     path = []
#     visited = set()
#     queue = deque([source])
#     visited.add(source)
    
#     while queue:
#         node = queue.popleft()
#         path.append(node)
        
#         for neighbor in sorted(graph[node]):
#             if neighbor not in visited:
#                 visited.add(neighbor)
#                 queue.append(neighbor)
#     return path

# output = BFS(graph, 1)
# print(" ".join(map(str, output)))

def bubble(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr




import sys
from queue import Queue

def BFS(source):
    visited = [0] * (N + 1)
    q = Queue()
    q.put(source)
    visited[source] = 1

    while not q.empty():
        u = q.get()
        print(u, end=' ')
        adj[u] = bubble(adj[u])
        for v in adj[u]:
            if visited[v] == 0:
                q.put(v)
                visited[v] = 1

#global N, M
N, M = map(int, sys.stdin.readline().split())
global adj
adj = [[] for i in range(N + 1)]

for i in range(M):
    u, v = map(int, sys.stdin.readline().split())
    adj[u].append(v)
    adj[v].append(u)

BFS(1)