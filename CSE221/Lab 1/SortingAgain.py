def selection_sort(arr1, arr2, n):
    c= 0
    for i in range(n):
        max= arr2[i]
        max_idx= i
        flag= False
        for j in range(i+1, n):
            if arr2[j] > max:
                max= arr2[j]
                max_idx= j
                flag= True
            elif arr2[j] == max:
                if arr1[j] < arr1[max_idx]:
                    max_idx= j
                    flag= True
        if flag is True:
            arr2[i], arr2[max_idx]= arr2[max_idx], arr2[i]
            arr1[i], arr1[max_idx]= arr1[max_idx], arr1[i]
            c += 1
    return c

n= int(input())
arr1= list(map(int, input().split()))
arr2= list(map(int, input().split()))

swaps = selection_sort(arr1, arr2, n)
print("Minimum swaps:", swaps)

for i in range(n):
    print(f"ID: {arr1[i]} Mark: {arr2[i]}")