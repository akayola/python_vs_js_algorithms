""" Sorting array using nested loop
    O(n^2) quadratic runtime complexity (BAD Solution)
    Sorting from end for array, at least dosn't compare sorted items
"""

def bubble_sort_nested_loop_improved(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            print(arr, arr[j], arr[j+1], i, j, j+1)
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

        print("ONE PASS COMPLETE")
    return arr

print(bubble_sort_nested_loop_improved([23, 12, 67, 5, 56, 34]))
#print(bubble_sort_nested_loop_improved([8, 1, 2, 3, 4, 5, 6, 7]))
