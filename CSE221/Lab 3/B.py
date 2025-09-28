#B # Count the inversion Revisited
'''
The program counts a special kind of “inversion-like” condition, 
but instead of directly comparing numbers from left and right halves, 
it works with squares of right-half elements 
and checks how many of them are smaller than each left-half element.
'''
import sys
def merge_sort(arr, left, right):
    if left >= right:
        return 0
    mid = (left+right)//2
    count = merge_sort(arr, left, mid)
    count += merge_sort(arr, mid+1, right)
    sqr = [arr[k]*arr[k] for k in range(mid+1, right+1)]
    sqr.sort()
    for i in range(left, mid+1):
        count += counting(sqr, arr[i])
    merge(arr, left, mid, right)
    return count

def merge(arr, left, mid, right):
    temp = []
    i = left
    j = mid+1
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1
    while i <= mid:
        temp.append(arr[i])
        i += 1
    while j <= right:
        temp.append(arr[j])
        j += 1
    for k in range(len(temp)):
        arr[left+k] = temp[k]

def counting(sq, res):
    low, high = 0, len(sq)
    while low < high:
        mid = (low+high)//2
        if sq[mid] < res:
            low = mid+1
        else:
            high = mid
    return low

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
print(merge_sort(arr, 0, n-1))
