# Given an integer array nums, find the subarray with the largest sum, and return its sum.

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
# Example 2:

# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
# Example 3:

# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

def largestSubarray(nums):
    res = 0
    largest = 0

    for num in nums:
        if num > res and num > 0:
            res = num
        elif (num + res) < 0:
            res = 0
        else:
            res += num
        if largest < res:
            largest = res
    return largest

print(largestSubarray([1]))
