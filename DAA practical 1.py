import time

# ==============================================================================
# DAA PRACTICAL 1: SORTING ALGORITHMS
# 1. Selection Sort
# 2. Bubble Sort
# 3. Merge Sort
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. SELECTION SORT
# ------------------------------------------------------------------------------
def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


# Execution & Demonstration for Selection Sort
arr_selection = [64, 34, 25, 12, 22, 11, 90]
print("--- 1. SELECTION SORT ---")
print("Original Array:", arr_selection)

start_time = time.perf_counter()
sorted_selection = selection_sort(arr_selection.copy())
end_time = time.perf_counter()

print("Sorted Array  :", sorted_selection)
print("Time Complexity:")
print("  Best Case   : O(n^2)")
print("  Average Case: O(n^2)")
print("  Worst Case  : O(n^2)")
print(f"Execution Time: {end_time - start_time:.8f} seconds\n")

"""
OUTPUT FOR SELECTION SORT:
--------------------------------------------------
--- 1. SELECTION SORT ---
Original Array: [64, 34, 25, 12, 22, 11, 90]
Sorted Array  : [11, 12, 22, 25, 34, 64, 90]
Time Complexity:
  Best Case   : O(n^2)
  Average Case: O(n^2)
  Worst Case  : O(n^2)
Execution Time: 0.00001530 seconds
--------------------------------------------------
"""


# ------------------------------------------------------------------------------
# 2. BUBBLE SORT
# ------------------------------------------------------------------------------
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


# Execution & Demonstration for Bubble Sort
arr_bubble = [64, 34, 25, 12, 22, 11, 90]
print("--- 2. BUBBLE SORT ---")
print("Original Array:", arr_bubble)

start_time = time.perf_counter()
sorted_bubble = bubble_sort(arr_bubble.copy())
end_time = time.perf_counter()

print("Sorted Array  :", sorted_bubble)
print("Time Complexity:")
print("  Best Case   : O(n)")
print("  Average Case: O(n^2)")
print("  Worst Case  : O(n^2)")
print(f"Execution Time: {end_time - start_time:.8f} seconds\n")

"""
OUTPUT FOR BUBBLE SORT:
--------------------------------------------------
--- 2. BUBBLE SORT ---
Original Array: [64, 34, 25, 12, 22, 11, 90]
Sorted Array  : [11, 12, 22, 25, 34, 64, 90]
Time Complexity:
  Best Case   : O(n)
  Average Case: O(n^2)
  Worst Case  : O(n^2)
Execution Time: 0.00000820 seconds
--------------------------------------------------
"""


# ------------------------------------------------------------------------------
# 3. MERGE SORT
# ------------------------------------------------------------------------------
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr


# Execution & Demonstration for Merge Sort
arr_merge = [64, 34, 25, 12, 22, 11, 90]
print("--- 3. MERGE SORT ---")
print("Original Array:", arr_merge)

start_time = time.perf_counter()
sorted_merge = merge_sort(arr_merge.copy())
end_time = time.perf_counter()

print("Sorted Array  :", sorted_merge)
print("Time Complexity:")
print("  Best Case   : O(n log n)")
print("  Average Case: O(n log n)")
print("  Worst Case  : O(n log n)")
print(f"Execution Time: {end_time - start_time:.8f} seconds\n")

"""
OUTPUT FOR MERGE SORT:
--------------------------------------------------
--- 3. MERGE SORT ---
Original Array: [64, 34, 25, 12, 22, 11, 90]
Sorted Array  : [11, 12, 22, 25, 34, 64, 90]
Time Complexity:
  Best Case   : O(n log n)
  Average Case: O(n log n)
  Worst Case  : O(n log n)
Execution Time: 0.00001370 seconds
--------------------------------------------------
"""
