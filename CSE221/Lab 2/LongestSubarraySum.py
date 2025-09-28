import sys
def longest_K_subarray(n, k, arr):
    x = 0
    sum = 0
    maximum = 0
    for i in range(n):
        sum += arr[i]
        if sum > k:
            sum -= arr[x]
            x += 1
        maximum = max(maximum, i-x+1)
    return maximum

n, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
print(longest_K_subarray(n, k, arr))