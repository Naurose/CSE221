def bubble_sort(arr):
    n = len(arr)
    for i in range(0, n):
        flag = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag = True
        if not flag:
            break

length = int(input())
arr = list(map(int, input().split()))
#print(f"Given array: {arr}")
# bubble_sort(arr)
# print(" ".join(map(str, arr)))

even_array = []
odd_array = []

for i in range(length):
    if i % 2 == 0:
        even_array.append(arr[i])
    else:
        odd_array.append(arr[i])

bubble_sort(even_array)
bubble_sort(odd_array)

new_array = [0]*length
even_idx = 0
odd_idx = 0

for i in range(length):
    if i%2 == 0:
        new_array[i] = even_array[even_idx]
        even_idx += 1
    else:
        new_array[i] = odd_array[odd_idx]
        odd_idx += 1

#print("Final merged array:", " ".join(map(str, new_array)))

is_sorted = True
for i in range(length - 1):
    if new_array[i] > new_array[i + 1]:
        is_sorted = False
        break

print("YES" if is_sorted else "NO")