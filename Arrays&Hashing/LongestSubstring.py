# Given a string s, find the length of the longest
# substring
#  without repeating characters.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        left, right = 0, 0
        max_length = 0
        window = set()

        while right < len(s):
            while s[right] in window:
                # run until window is valid again
                window.discard(s[left])
                left += 1

            max_length = max(max_length, right-left+1)
            window.add(s[right])
            right += 1

        return max_length
