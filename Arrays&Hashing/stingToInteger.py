class Solution:
    def myAtoi(self, s: str) -> int:
        # Step 1: Remove leading and trailing whitespace
        s = s.strip()

        # If string is empty after stripping, return 0
        if not s:
            return 0

        # Step 2: Determine sign
        sign = 1
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]

        # Step 3: Read numeric characters until non-digit or end of string
        num = 0
        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            else:
                break

        # Step 4: Apply sign and handle overflow
        num = sign * num
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        if num > INT_MAX:
            return INT_MAX
        elif num < INT_MIN:
            return INT_MIN
        else:
            return num
