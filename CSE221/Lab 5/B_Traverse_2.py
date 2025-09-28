import sys
from collections import defaultdict
input = sys.stdin.readline
sys.setrecursionlimit(2*100000+5)

graph = defaultdict(list)

N, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

for u, v in zip(a, b):
    graph[u].append(v)
    graph[v].append(u)

for node in graph:
    graph[node].sort()

def DFS(tree, node, path, visited):
    visited.add(node)
    path.append(node)

    for child in tree[node]:
        if child not in visited:
            DFS(tree, child, path, visited)
    return path

visited = set()
path = []
print(*DFS(graph, 1, path, visited))