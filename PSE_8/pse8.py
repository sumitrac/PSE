# Given an array arr of positive integers sorted 
# in a strictly increasing order, and an integer k.
# Find the kth positive integer that is missing from this array.

# Input: arr = [2,3,4,7,11], k = 5
# Output: 9
# Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. 
# The 5th missing positive integer is 9.

# Constraints:
# 1 <= arr.length <= 1000
# 1 <= arr[i] <= 1000
# 1 <= k <= 1000
# arr[i] < arr[j] for 1 <= i < j <= arr.length

numbers = [ 4, 5, 7, 9]
k = 2 # 2nd number is missing 
# output = 2 
# explanation: The missing positive integers are [1, 2, 3, 6, 8...]

numbers = [1, 2, 5, 8, 9, 20]
k = 10 # 10th number is missing 
# output = 15
# explanation: the missing positive integers are [3, 4, 6, 7, 10, 11, 12, 13, 14, 15...]

numbers = [1, 3, 5, 7]
k = 3 # 3rd number is missing 
#missing number is 4: [2, 4...]
#explanation: the missing positive integers are [1, ]

def kth_missing_positive_number(numbers, k):
    len_array = len(numbers)
    i = 0
    j = 1
    skip = 0

    while i < len_array:
        if numbers[i] != j:
            skip += 1
            if k == skip:
                return j 
            else: 
                i += 1
                j += 1
        return numbers[-1] + (k-skip)

    # min_len = 0
    # max_len = len(numbers)
    # missing_int = []

    # while min_len < max_len:
    #     missing = min_len + (max_len - 1) // 2
    #     #print(missing) 
    #     if numbers[missing] - (missing + 1) >= k: 
    #         #max_len = missing
    #         print(max_len)
    #     else: 
    #         min_len = missing + 1
    #         #print(min_len)
    #         missing_int.append(min_len + k)
    #         print(missing_int)

print(kth_missing_positive_number(numbers, k))

#Time Complexity O(n)
#Space complexity O(n)

