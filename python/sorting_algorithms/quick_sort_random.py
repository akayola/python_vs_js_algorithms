import random

def partition_random(arr, start, end):
    random_pivot = random.randrange(start, end)

    arr[start], arr[random_pivot] = arr[random_pivot], arr[start]
    print(f'arr: {arr}, pivot: {arr[0]}, random_pivot_index: {random_pivot}')
    
    return partition(arr, start, end)


def partition(arr, start, end):
    pivot = arr[start]
    swap_index =  start

    for i in range(start + 1, end + 1):
        if arr[i] <= pivot:
            swap_index += 1
            arr[swap_index], arr[i] = arr[i], arr[swap_index] 
            #swap_index += 1

    arr[start], arr[swap_index] = arr[swap_index], arr[start]

    return swap_index

def quick_sort(arr, start, end):
    if start < end:
        pivot_index = partition_random(arr, start, end)
        #pivot_index = partition(arr, start, end)
        quick_sort(arr, start, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, end)
    return arr


#arr1 = [23, 41, 4, 56, 8, 98, 12, -10, 9, -12]
#arr1 = [23, 4, -10]
#arr1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1,]
arr1 = [1,2,3,4,5,6,7,8,9,10]

print(f'{quick_sort(arr1, 0, len(arr1) - 1)}')
