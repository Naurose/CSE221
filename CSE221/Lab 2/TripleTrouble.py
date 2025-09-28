import sys
N, x = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
indexed_A = [(val, idx) for idx, val in enumerate(A)]
indexed_A.sort()  
best = None

for i in range(N):
    for j in range(i+1, N):
        target = x - (indexed_A[i][0] + indexed_A[j][0])
        l, r = j+1, N-1
        while l <= r:
            m = (l + r) // 2
            if indexed_A[m][0] == target:
                triplet = sorted([indexed_A[i][1]+1, indexed_A[j][1]+1, indexed_A[m][1]+1])
                triplet = tuple(triplet)
                if not best or triplet < best:
                    best = triplet
                break
            elif indexed_A[m][0] < target:
                l = m + 1
            else:
                r = m - 1

if best:
    print(*best)
else:
    print(-1)