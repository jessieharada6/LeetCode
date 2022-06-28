class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        res = math.inf
        memo = [[66666] * n for _ in range(n)]
        
        def dp(i, j):
            if i < 0 or j < 0 or i >= n or j >= n:
                return 66666                  # sum range: [-10000, 10000], get a larger number 
            
            if i == 0:
                return matrix[0][j]
            
            if memo[i][j] != 66666:
                return memo[i][j]
            
            memo[i][j] = matrix[i][j] + min(dp(i - 1, j), dp(i - 1, j - 1), dp(i - 1, j + 1))
            return memo[i][j]
            
        
        for j in range(n):
            res = min(res, dp(n - 1, j))        # select the min on the row
        
        return res
            