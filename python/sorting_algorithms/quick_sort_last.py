def partition_last(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            (arr[i], arr[j]) = (arr[j], arr[i])

    (arr[i + 1], arr[high]) = (arr[high], arr[i + 1])
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition_last(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)
    return arr

arr1 = [22, 14, 41, 67, 23, 45, 12, 16, 56, 17]

print(partition_last(arr1, 0, len(arr1) -1))
print(quick_sort(arr1, 0, len(arr1) - 1))

arr1 = [i for i in range(10, 0, -1)]
print(quick_sort(arr1, 0, len(arr1) - 1))

arr1 = [i for i in range(1,11)]
print(quick_sort(arr1, 0, len(arr1) - 1))
