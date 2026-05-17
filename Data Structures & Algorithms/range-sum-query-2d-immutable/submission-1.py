class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.sumMat = [[0] * (len(matrix[0])+1) for _ in range(len(matrix)+1)]
        for i in range(len(matrix)):
            prefix = 0
            for j in range(len(matrix[0])):
                prefix += matrix[i][j]
                above = self.sumMat[i][j+1]
                self.sumMat[i+1][j+1] = prefix + above


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.sumMat[row2+1][col2+1] + self.sumMat[row1][col1] - self.sumMat[row1][col2+1] - self.sumMat[row2+1][col1]