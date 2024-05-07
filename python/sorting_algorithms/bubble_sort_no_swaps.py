""" Sorting array using nested loop
    O(n^2) quadratic runtime complexity (BAD Solution)
    Sorting from end for array, at least dosn't compare sorted items
    Added no_swaps for array almost sorted
"""

def bubble_sort_nested_loop_no_swaps(arr):
    for i in range(len(arr) - 1, 0, -1):
        no_swaps = True
        for j in range(i):
            print(arr, arr[j], arr[j+1], i, j, j+1)
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                no_swaps = False

        if no_swaps: break
        print("ONE PASS COMPLETE")
    return arr

#print(bubble_sort_nested_loop_no_swaps([8, 1, 2, 3, 4, 5, 6, 7]))
print(bubble_sort_nested_loop_no_swaps([23, 12, 67, 5, 56, 34]))
