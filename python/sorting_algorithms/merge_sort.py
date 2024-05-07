# merge sort

def merge(arr1, arr2):
    results = []
    i = 0 
    j = 0

    while i < len(arr1) and j < len(arr2):
        if arr2[j] > arr1[i]:
            results.append(arr1[i])
            i += 1
        else:
            results.append(arr2[j])
            j += 1
    while i < len(arr1):
        results.append(arr1[i])
        i += 1
    while j < len(arr2):
        results.append(arr2[j])
        j += 1
    return results

print(merge([1,2,3,4], [7,8,9,10]))


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[0:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


print(merge_sort([98, -12, -2, 87, 23, 15, 45, -4, 67, 34]))
