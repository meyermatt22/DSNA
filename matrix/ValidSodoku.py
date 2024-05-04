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

              
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                seen = set()
                for x in range(3):
                    for y in range(3):
                        num = board[i + x][j + y]
                        if num != ".":
                            if num in seen:
                                return False
                            seen.add(num)


        return True
