#187

# The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

# For example, "ACGAATTCCG" is a DNA sequence.
# When studying DNA, it is useful to identify repeated sequences within the DNA.

# Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.


from typing import List
from collections import defaultdict

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:

        if len(s) < 10:
            return []

        sequence_count = defaultdict(int)
        repeated_sequences = set()

        for i in range(len(s) - 9):
            sequence = s[i:i + 10]
            sequence_count[sequence] += 1

            if sequence_count[sequence] > 1:
                repeated_sequences.add(sequence)

        return list(repeated_sequences)
