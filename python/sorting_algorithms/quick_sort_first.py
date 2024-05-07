def partition(arr, start, end):
    pivot = arr[start]
    swap_index = start + 1
    print(f'arr: {arr}, pivot: {pivot}, start: {start}, swap_index: {swap_index}')

    for i in range(start + 1, end + 1):
        # print(pivot, i, arr[i] )
        # if arr[i] <= pivot:
        if pivot >= arr[i]:
            arr[i], arr[swap_index] = arr[swap_index], arr[i]
            # print(arr, i, swap_index)
            swap_index += 1

    arr[start], arr[swap_index - 1] = arr[swap_index - 1], arr[start]
    # print(arr, pivot, swap_index - 1)
    return swap_index - 1


def quick_sort(arr, start, end):
    if start < end:
        pivot_index = partition(arr, start, end)
        quick_sort(arr, start, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, end)
    return arr


arr1 = [26, 14, 78, 19, 99, 35, 26, 36, 37, 2]

# print(partition(arr1, 0, len(arr1) - 1))
print(quick_sort(arr1, 0, len(arr1) - 1))
