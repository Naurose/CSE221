import sys
def upper(arr, low, high, x, value = -1):
    if high >= low:
        mid = low + (high-low)//2
        if arr[mid] <= x:
            value = mid 
            return upper(arr, mid+1, high, x, value)
        else:
            return upper(arr, low, mid-1, x, value)
    return value

def lower(arr, low, high, x, value = -1):
    if high >= low:
        mid = low + (high - low) // 2
        if arr[mid] >= x:
            value = mid
            return lower(arr, low, mid-1, x, value)
        else:
            return lower(arr, mid+1, high, x, value)
    return value 


length, n = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))
for i in range(n):
    l, u = map(int, sys.stdin.readline().split())
    upper_bound = upper(arr, 0, length-1, u) 
    lower_bound = lower(arr, 0, length-1, l) 
    if lower_bound == -1 or upper_bound == -1:
        print(0)
    else:
        print(upper_bound - lower_bound + 1)