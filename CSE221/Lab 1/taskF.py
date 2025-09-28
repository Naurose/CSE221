def sorting_algo(arr):
    n = len(arr)

    while True:
        flag = False
        for i in range(n-1):
            if (arr[i]%2 == arr[i+1]%2) and (arr[i] > arr[i+1]):
                arr[i], arr[i+1] = arr[i+1], arr[i]
                flag = True
        if flag != True:
            break
    return arr

n = int(input())
arr = list(map(int, input().split()))
sorting_algo(arr)
print(" ".join(map(str, arr)))