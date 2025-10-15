def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr if x < pivot]  # ❌ Includes pivot again
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

print(quick_sort([3, 6, 8, 10, 1, 2, 1]))  # Expected [1, 1, 2, 3, 6, 8, 10]
