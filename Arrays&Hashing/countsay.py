# The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

# countAndSay(1) = "1"
# countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.
# To determine how you "say" a digit string, split it into the minimal number of substrings such that each substring contains exactly one unique digit. Then for each substring, say the number of digits, then say the digit. Finally, concatenate every said digit.

# For example, the saying and conversion for digit string "3322251":


class Solution:
    def countAndSay(self, n: int) -> str:

        if n == 1:
            return "1"

        prev = self.countAndSay(n - 1)

        result = ""
        count = 1

        for i in range(1, len(prev)):

            if prev[i] != prev[i - 1]:

                result += str(count) + prev[i - 1]
                count = 1
            else:
                count += 1

        result += str(count) + prev[-1]

        return result
