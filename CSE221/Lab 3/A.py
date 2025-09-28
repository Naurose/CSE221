#A #Count the Inversion 
import sys
def mergeSort(arr, left, right):
    count = 0
    if left < right:
        mid = (left + right) // 2
        count += mergeSort(arr, left, mid)  
        count += mergeSort(arr, mid + 1, right)  
        count += merge(arr, left, mid, right) 
    return count

def merge(arr, left, mid, right):
    count = 0
    temp = [] 
    i = left
    j = mid + 1

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1
            count += (mid + 1 - i )
    
    while i <= mid:
        temp.append(arr[i])
        i += 1
    while j <= right:
        temp.append(arr[j])
        j += 1
    for k in range(len(temp)):
        arr[left + k] = temp[k]
    return count

n = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().split()))
print(mergeSort(arr, 0, n - 1))
print(" ".join(map(str, arr))) 