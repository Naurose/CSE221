#Friendship
import sys
input = sys.stdin.readline

def find(x):
    r = x
    while parent[r] != r:
        r = parent[r]
    while parent[x] != r:
        parent[x] = r
        x = parent[x]
    return r

def union(a, b):
    r_a = find(a)
    r_b = find(b)

    if r_a != r_b:
        if size[r_a] < size[r_b]:
            r_a, r_b = r_b, r_a
        parent[r_b] = r_a
        size[r_a] += size[r_b]
    return size[r_a]

N, K = map(int, input().split())
parent = [i for i in range(N+1)]
size = [1] * (N+1)

for i in range(K):
    a, b = map(int, input().split())
    print(union(a, b))