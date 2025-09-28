#Minimum Spanning Tree
import sys
from collections import deque
input = sys.stdin.readline

def make_set(n):
    return list(range(n + 1)), [1] * (n + 1)

def find(parent, i):
    root = i
    # Path compression - find root
    while root != parent[root]:
        root = parent[root]
    # Path compression - update nodes
    while i != root:
        next_parent = parent[i]
        parent[i] = root
        i = next_parent
    return root

def union(parent, rank, x, y):
    s1 = find(parent, x)
    s2 = find(parent, y)
    if s1 != s2:
        if rank[s1] < rank[s2]:
            parent[s1] = s2
        elif rank[s1] > rank[s2]:
            parent[s2] = s1
        else:
            parent[s2] = s1
            rank[s1] += 1
        return True
    return False

def kruskal(n, edges, exclude_edge=None):
    parent, rank = make_set(n)
    mst_cost = 0
    mst_edges = []
    edges_used = 0

    for u, v, w in edges:
        if edges_used == n - 1:
            break
        if (u, v, w) == exclude_edge or (v, u, w) == exclude_edge:
            continue
        if union(parent, rank, u, v):
            mst_cost += w
            mst_edges.append((u, v, w))
            edges_used += 1

    # Check if MST is valid
    root = find(parent, 1)
    for i in range(2, n + 1):
        if find(parent, i) != root:
            return None, None
    return mst_cost, mst_edges

def find_max_edge(adj, start, end, n):
    visited = [False] * (n + 1)
    q = deque([(start, 0)])
    visited[start] = True
    max_weights = [0] * (n + 1)
    parent = [-1] * (n + 1)

    while q:
        u, max_so_far = q.popleft()
        if u == end:
            return max_so_far

        for v, w in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                max_weights[v] = max(max_so_far, w)
                q.append((v, max_weights[v]))
    return None

def find_second_mst(n, edges):
    edges.sort(key=lambda x: x[2])  # Sort by weight
    mst_cost, mst_edges = kruskal(n, edges)
    
    if mst_cost is None:
        return -1

    second_best = float('inf')
    mst_set = {(u, v, w) for u, v, w in mst_edges} | {(v, u, w) for u, v, w in mst_edges}
    
    # Build adjacency list
    adj = [[] for _ in range(n + 1)]
    for u, v, w in mst_edges:
        adj[u].append((v, w))
        adj[v].append((u, w))

    # Try excluding each MST edge
    for edge in mst_edges:
        cost, _ = kruskal(n, edges, exclude_edge=edge)
        if cost and cost > mst_cost:
            second_best = min(second_best, cost)

    # Try non-MST edges
    for edge in edges:
        if edge not in mst_set:
            u, v, w = edge
            max_edge = find_max_edge(adj, u, v, n)
            if max_edge is not None:
                new_cost = mst_cost + w - max_edge
                if new_cost > mst_cost:
                    second_best = min(second_best, new_cost)

    return second_best if second_best != float('inf') else -1

# Read input
N, M = map(int, input().split())
edges = []
for _ in range(M):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))

# Print result
print(find_second_mst(N, edges))