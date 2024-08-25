# Compare arrays
# arr2.index is nested loop of for loop, O(n^2) runtime complexity.
# we should avoid using nested loops.

def same(arr1, arr2):
    if len(arr1) != len(arr2):
        return False
    for i in range(len(arr1)):
        try:
            correct_index = arr2.index(arr1[i] ** 2)
        except ValueError:
            return False
        else:
            if not isinstance(correct_index, int):
                return False
            else:
                #print(arr2)
                arr2.pop(correct_index)
    return True

print(same([3, 4, 5, 6], [16, 36, 9, 25]))
print(same([3, 4, 5, 6], [1, 15, 25, 36]))