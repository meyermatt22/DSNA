# Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

# Since the result may be very large, so you need to return a string instead of an integer.



# Example 1:

# Input: nums = [10,2]
# Output: "210"
# Example 2:

# Input: nums = [3,30,34,5,9]
# Output: "9534330"

# Constraints:

# 1 <= nums.length <= 100
# 0 <= nums[i] <= 109

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(x, y):
            return int(y + x) - int(x + y)

        nums_str = [str(num) for num in nums]
        nums_str.sort(key=cmp_to_key(compare))

        if nums_str[0] == "0":
            return "0"

        return "".join(nums_str)
