def partition(arr, low, high):
    pivot = arr[low]
    start = low + 1
    end = high

    while True:
        while start <= end and arr[end] >= pivot:
            end -= 1
        while start <= end and arr[start] <= pivot:
            start += 1

        if start <= end:
            arr[start], arr[end] = arr[end], arr[start]
        else:
            break
    arr[low], arr[end] = arr[end], arr[low]
    return end

def quick_sort(arr, start, end):
    if start < end: 
        pivot_index = partition(arr, start, end)
        quick_sort(arr, start, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, end)
    return arr

#arr1 = [4, 8, 2, 1, 5, 7, 6, 3]
arr1 = [4, -8, 2, 1, 0.5, 7, 6, 3, 0.49]
#print(partition(arr1, 0, len(arr1) - 1))
print(quick_sort(arr1, 0, len(arr1) - 1))

#arr1 = [26, 40, 41, 14, 18, 78, 19, 99]
#print(quick_sort(arr1, 0, len(arr1) - 1))

arr1 = [i for i in range(10, -1, -1)]
print(quick_sort(arr1, 0, len(arr1) - 1))
