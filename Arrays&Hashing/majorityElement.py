# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.



# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        numNums = {}

        for num in nums:
            if num in numNums:
                numNums[num] += 1
            else:
                numNums[num] = 1

        max_key = max(numNums, key=numNums.get)
        max_value = numNums[max_key]

        if max_value > n / 2:
            return max_key

        return False 
