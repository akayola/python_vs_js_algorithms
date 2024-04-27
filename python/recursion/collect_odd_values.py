# Collect odd values using helper method recursion

def collect_odd_values(arr):

    result = []

    def helper(helper_input):

        if len(helper_input) == 0:
            return
   
        if helper_input[0] % 2 != 0:
            result.append(helper_input[0])

        helper(helper_input[1:])

    helper(arr)
    return result

print(collect_odd_values([1, 2, 3, 4, 5, 6, 7, 8, 9]))     
