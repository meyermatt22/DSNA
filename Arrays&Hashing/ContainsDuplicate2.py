# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        window = set()
        left = 0

        for right in range(len(nums)):
            if right - left > k:
                window.discard(nums[left])
                left += 1

            if nums[right] in window:
                return True
            window.add(nums[right])

        return False
