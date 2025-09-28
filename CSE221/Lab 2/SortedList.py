import sys

def SortedList(arr1, arr2, len1, len2):
    i = 0
    j = 0
    arr3 = []
    count = len1 + len2

    while i != len1 and j  != len2:
        if arr1[i] <= arr2[j]:
            arr3.append(arr1[i])
            i += 1
            count += 1
        elif arr1[i] > arr2[j]:
            arr3.append(arr2[j])
            j += 1
            count += 1
    if count + 1 != len(arr3):
        if i == len1:
            for j in range(j, len2):
                arr3.append(arr2[j])
        else:
            for i in range(i, len1):
                arr3.append(arr1[i])
    
    return arr3

len1 = int(sys.stdin.readline())
arr1 = list(map(int,sys.stdin.readline().split()))
len2 = int(sys.stdin.readline())
arr2 = list(map(int,sys.stdin.readline().split()))
arr3 = SortedList(arr1, arr2, len1, len2)

sys.stdout.write(" ".join(map(str, arr3)))