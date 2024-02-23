# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        num_set = set(nums) 
        longest = 0

        for n in nums:
            if(n-1) not in num_set:
                length = 0

                while (n+length) in num_set:
                    length += 1

            longest = max(length, longest)

        return longest

