"""
   In selection sorting algorithms:
   1. Find smallest item
   2. Move smallest item to the beginning of array
   3. Perform same steps for rest of items
"""

def selection_sort(arr):
    for i in range(len(arr)):
        smallest = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest]:
                smallest = j
       
        #Swapping arr[smallest] with arr[i]
        if i != smallest:
            print("**********")
            print(arr)
            print("SWAPPING TO")
            arr[i], arr[smallest] = arr[smallest], arr[i]
            print(arr)
            print("**********")

    return arr
   
print(selection_sort([23, 16, 56, 18, 67, 32]))
