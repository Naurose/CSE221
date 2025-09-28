#F #Ordering Binary Tree
import sys
def balanced_bst(arr, left, right, result):
    if left > right:
        return
    mid = (left + right) // 2
    result.append(arr[mid])
    balanced_bst(arr, left, mid - 1, result)
    balanced_bst(arr, mid + 1, right, result)

n = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().split()))
result = []
balanced_bst(arr, 0, n - 1, result)
print(" ".join(map(str, result)))