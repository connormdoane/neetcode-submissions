class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        extraBit = 1
        rows, cols = len(matrix), len(matrix[0])

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    if r == 0:
                        extraBit = 0
                        continue
                    matrix[r][0] = 0
                    matrix[0][c] = 0
        
        for r in range(1, rows):
            if matrix[r][0] == 0:
                for c in range(cols):
                    matrix[r][c] = 0
        for c in range(cols):
            if matrix[0][c] == 0:
                for r in range(rows):
                    matrix[r][c] = 0
        
        if not extraBit:
            for c in range(cols):
                matrix[0][c] = 0
