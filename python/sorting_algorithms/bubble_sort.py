"""
   Bubble sorting algorithm:
   1. Find beggest item and move to end for array.
   2. Perform same for rest of items. 
   Using nested loop, O(n^2) quadratic runtime complexity (bad solution).
   Running from beginning of array, comparing already sorted items.
"""

def bubble_sort_nested_loop(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1):
            print(arr, arr[j], arr[j + 1], i, j, j+1)
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        print("ONE PASS COMPLETE")
    return arr

print(bubble_sort_nested_loop([23, 12, 67, 5, 56, 34]))
