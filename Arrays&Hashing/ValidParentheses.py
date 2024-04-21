# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []

        close_to_open = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        for char in s:
            if char not in close_to_open:
                stack.append(char)
            elif not stack or stack[-1] != close_to_open[char]:
                return False
            else:
                stack.pop()

        return len(stack) == 0
