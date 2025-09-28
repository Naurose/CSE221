def find_transition_to_decreasing(arr):
    low, high = 1, len(arr) - 1  # start from index 1 to compare with i-1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < arr[mid - 1]:
            # This is the start of the decreasing transition
            return mid
        elif arr[mid] > arr[0]:
            low = mid + 1
        else:
            high = mid - 1
    return -1  # No decreasing transition found

# Example usage:
arr = [9, 12, 15, 2, 4, 5, 7, 8]
index = find_transition_to_decreasing(arr)
print(f"Transition to decreasing occurs at index: {index}")
