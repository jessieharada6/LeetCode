class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]
        
        for i in range(1, m):
            dp[i][0] = grid[i][0] + dp[i - 1][0]
        
        for j in range(1, n):
            dp[0][j] = grid[0][j] + dp[0][j - 1]
        
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])
               
        return dp[-1][-1]

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        memo = [[-1] * n for _ in range(m)]
        
        def dp(i, j):   
            if i == 0 and j == 0:
                return grid[0][0]
            
            if i < 0 or j < 0:
                return math.inf
            
            if memo[i][j] != -1:
                return memo[i][j]
            
            memo[i][j] = grid[i][j] + min(dp(i - 1, j), dp(i, j - 1))
            return memo[i][j]
        
        return dp(m - 1, n - 1)
        