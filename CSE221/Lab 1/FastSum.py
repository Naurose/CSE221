# T = int(input())

# for i in range (T):
#     N = int(input())
#     sum = 0

#     for j in range(1, N+1):
#         sum += j
#     print(sum)

# import sys
# T = int(sys.stdin.readline().strip())
# for i in range(T):
#     N = int(sys.stdin.readline().strip())
#     print(N * (N + 1) // 2) 


import sys
import time
start = time.time()

# Your code here
T = int(sys.stdin.readline().strip())
for i in range(T):
    N = int(sys.stdin.readline().strip())
    print(N * (N + 1) // 2) 

end = time.time()
print(f"Runtime: {(end - start)*1000:.2f} ms")
