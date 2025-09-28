import sys
N, M, x = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

i = 0
j = M - 1
v1 = 0
v2 = 0
diff = float('inf')

while i < N and j >= 0:
    s = A[i] + B[j]
    if abs(s-x) < diff:
        diff = abs(s-x)
        v1 = i
        v2 = j
    if s < x:
        i += 1
    else:
        j -= 1
        
print(v1 + 1, v2 + 1)