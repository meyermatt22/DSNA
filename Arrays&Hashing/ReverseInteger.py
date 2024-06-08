# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).



# Example 1:

# Input: x = 123
# Output: 321
# Example 2:

# Input: x = -123
# Output: -321
# Example 3:

# Input: x = 120
# Output: 21

class Solution:
    def reverse(self, x: int) -> int:

        negative = x < 0

        str_x = str(abs(x))

        reversed_str = str_x[::-1]

        reversed_x = int(reversed_str)

        if negative:
            reversed_x *= -1

        if reversed_x < -2**31 or reversed_x > 2**31 - 1:
            return 0

        return reversed_x
