import math
from itertools import chain

#Returns digit at position index i
#index 0 starting from right (least significant digit)
def get_digit(num, i):
    return abs(num) // pow(10, i) % 10

#Returns number of digits
def digit_count(num):
    if num == 0: return 1
    return math.floor(math.log10(abs(num))) + 1

#Returns max number of digits of the largest number
def most_digits(nums):
    max_digits = 0

    for i in range(len(nums)):
        max_digits = max(max_digits, digit_count(nums[i]))
    return max_digits


def radix_sort(nums):
    max_digit_count = most_digits(nums)

    for k in range(max_digit_count):
        digit_buckets = [[] for _ in range(10)]
        for i in range(len(nums)):
            digit = get_digit(nums[i], k)
            digit_buckets[digit].append(nums[i])

        print(digit_buckets)
        nums = list(chain.from_iterable(digit_buckets))
        print(nums)

    return nums 

arr1 = [21, 999, 78, 3, 456, 215, 102, 198314, 17, 10]

print(radix_sort(arr1))
