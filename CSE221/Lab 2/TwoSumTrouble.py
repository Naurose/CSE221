import sys

def TwoSum(length, arr, sum):
    i = 0
    j = length - 1

    while i < j:
        if arr[i] + arr[j] == sum:
            return (f"{i + 1} {j + 1}")
        elif arr[i] + arr[j] > sum:
            j -= 1
        elif arr[i] + arr[j] < sum:
            i += 1
    
    return -1

length, sum = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))
print(TwoSum(length, arr, sum))