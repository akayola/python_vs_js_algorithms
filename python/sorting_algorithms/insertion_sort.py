"""
   Insertion Sort Algorithm
   Builds up the sort by gradually creating larger left helf,
   which is always sorted.
   It takes element and insert into sorted portion of the array.
   Pseudocode:
   1. Start picking second element in the array.
   2. Compare to element before and swap if necessary, this creates left sorted portion.
   3. Continue to next element compare to previous two sorted elements,
   and if smaller insert into proper position of sorted elements.
   4. Repeat until the array is sorted.
   O(n) - Best case for already sorted arrays, bacuse x < arr[j]  False, so algorithm will not go into while loop.
   O(n^2) - Worst case for reverse sorted arrays.
"""

def insertion_sort(arr):
    for i in range(1, len(arr)):
        x = arr[i]
        j = i - 1
        while j >= 0 and x < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = x
    return arr

print(insertion_sort([23, 12, 44, 5, 67, 34])) 
