#Ancient Ordering
import sys
import heapq
from collections import defaultdict, deque
input = sys.stdin.readline

N = int(input())
S = [input().strip() for i in range(N)]
graph = defaultdict(list)
degree = defaultdict(int)

store = set()

for i in range(len(S)-1):
    if len(S[i]) > len(S[i+1]):
        if S[i][:len(S[i+1])] == S[i+1]:
            print(-1)
            exit()
    
    flag = False
    for j in range(min(len(S[i]), len(S[i+1]))):
        if S[i][j] != S[i+1][j]:
            graph[S[i][j]].append(S[i+1][j])
            degree[S[i+1][j]] += 1
            flag = True
            break

for word in S:
    for c in word:
        store.add(c)
min_heap = []

for char in store:
    if degree[char] == 0:
        heapq.heappush(min_heap, char)
result = []

while min_heap:
    char = heapq.heappop(min_heap)
    result.append(char)
    for i in graph[char]:
        degree[i] -= 1
        if degree[i] == 0:
            heapq.heappush(min_heap, i)

if len(result) != len(store):
    print(-1)
else:
    print(''.join(result))