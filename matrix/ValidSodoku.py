class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row in board:
            inRow = set()
            for num in row:
                if num != inRow:
                    inRow.add(num)
                else:
                    return False

        for col in range(9):
            column = [board[i][col] for i in range(9)]
            inColumn = set()
            inRow = set()
            for num in column:
                if num != inColumn:
                    inColumn.add(num)
                else:
                    return False

        return True
