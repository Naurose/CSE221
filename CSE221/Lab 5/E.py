import sys
from collections import defaultdict
input = sys.stdin.readline

N, R = map(int,input().split())
adj = defaultdict(list)

for i in range(N-1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

subtree = [0] * (N + 1)

def DFS(u, parent):
    subtree[u] = 1
    for v in adj[u]:
        if v != parent:
            DFS(v, u)
            subtree[u] += subtree[v]
DFS(R, -1)

Q = int(input())
for i in range(Q):
    u = int(input())
    print(subtree[u])