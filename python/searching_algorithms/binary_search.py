# Binary search only works on sorted array.
# O(logn) runtime complexity.

def binary_search(arr, val):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] > val:
            end = mid - 1
        elif arr[mid] < val:
            start = mid + 1
        else:
            return mid
    return False

states = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]

print(binary_search([1, 22, 3, 45, 65, 67, 23, 98, 123, 17], 98))
print(binary_search([1, 22, 3, 45, 65, 67, 23, 98, 123, 17], 100))
print(binary_search(states, "North Dakota"))
