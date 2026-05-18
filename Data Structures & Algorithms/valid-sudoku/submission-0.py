class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)): # 0-8
            row = set()
            col = set()
            grid = set()
            for j in range(len(board)):
                rowval = board[i][j]
                colval = board[j][i]
                gridval = board[(3*(i%3))+j//3][3*(i%3)+j%3]
                if rowval != '.':
                    if rowval in row:
                        return False
                    else:
                        row.add(rowval)
                if colval != '.':
                    if colval in col:
                        return False
                    else:
                        col.add(colval)
                if gridval != '.':
                    if gridval in grid:
                        print(gridval, i, j)
                        return False
                    else:
                        grid.add(gridval)
        return True

            