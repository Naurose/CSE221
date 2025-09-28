import sys
def longest_K_subarray(N, K, arr):
    i = 0
    var = 0
    arr1 = [0]*(N+1) 
    sum = 0
    for j in range(N):
        if arr1[arr[j]] == 0:
            sum += 1
        arr1[arr[j]] += 1

        while sum > K and i <= j:
            arr1[arr[i]] -= 1
            if arr1[arr[i]] == 0:
                sum -= 1
            i += 1

        var = max(var, j-i+1)
    return var

length, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
print(longest_K_subarray(length, k, arr))