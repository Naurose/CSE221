#Help the King
import sys
input = sys.stdin.readline

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]  
        x = parent[x]
    return x
 
def union(a, b):
    r_a = find(a)
    r_b = find(b)
    if r_a == r_b:
        return False
    if size[r_a] < size[r_b]:
        r_a, r_b = r_b, r_a
    parent[r_b] = r_a
    size[r_a] += size[r_b]
    return True
 
 
N, M = map(int, input().split())
edges = []

for i in range(M):
    u, v, w = map(int, input().split())
    edges.append((w, u, v))
edges.sort()  
 
parent = [i for i in range(N + 1)]
size = [1] * (N + 1)
 
total = 0
for w, u, v in edges:
    if union(u, v):
        total += w
 
print(total)