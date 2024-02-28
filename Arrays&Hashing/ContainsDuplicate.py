# Given an integer array nums,
# return true if any value appears at least twice in the array,
# and return false if every element is distinct.

class Solution(object):
    def containsDuplicate( nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        newSet = set()

        for n in nums:
            if n in newSet:
                return True
            newSet.add(n)
        return False

    print(containsDuplicate( [1,2,3,4]))
    print(containsDuplicate( [1,2,3,1,4]))


# Solution([1,2,3,4])
# Solution([1,2,3,4,1])
