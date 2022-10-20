class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.presum = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]
        
        for i in range(1, len(self.presum)):
            for j in range(1, len(self.presum[0])):
                self.presum[i][j] += self.presum[i][j - 1] + self.presum[i - 1][j] - self.presum[i - 1][j - 1] + matrix[i - 1][j - 1]
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.presum[row2 + 1][col2 + 1] - self.presum[row2 + 1][col1] - self.presum[row1][col2 + 1] + self.presum[row1][col1]
        
        # sumresgoin(1,1,2,2)
        # [0, 0,  0,  0,  0, 0]
        # [0, 3,  3,  4,  8,  10]   -4: (1, 3)  +3(1,1)
        # [0, 8,  14, 18, 24, 27]
        # [0, 9,  17, 21, 28, 36]   -9:(3, 1)  21(3, 3)
        # [0, 13, 22, 26, 34, 49]
        # [0,  0,  0,  0, 0,  58]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)