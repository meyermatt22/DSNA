# Given an m x n grid of characters board and a string word, return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.



# Example 1:


# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # base cases
        #   1. if we find the word, return True
        #         a. if i == len(word)
        #   2. False
        #         a. out of bounds
        #         b. letter doesnt match word[i]
        #         c. return False if visited

        ROWS, COLS = len(board), len(board[0])
        visited = set()

        def _backtrack(r, c, i):
            if i == len(word):
                return True

            if not _inbound(r,c) or word[i] != board[r][c] or (r, c) in visited:
                return False

            # modifying
            visited.add((r, c))

            # recursion
            res = (_backtrack(r+1, c, i+1) or
                _backtrack(r-1, c, i+1) or
                _backtrack(r, c+1, i+1) or
                _backtrack(r, c-1, i+1))

            # backtrack
            visited.discard((r,c))

            return res

        def _inbound(r, c):
            rowInbound = r >= 0 and r < ROWS
            colInbound = c >= 0 and c < COLS
            return rowInbound and colInbound

        for r in range(ROWS):
            for c in range(COLS):
                if _backtrack(r, c, 0):
                    return True

        return False
