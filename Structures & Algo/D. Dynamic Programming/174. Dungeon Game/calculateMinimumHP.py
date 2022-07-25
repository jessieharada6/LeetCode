class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m = len(dungeon)
        n = len(dungeon[0])
        
        memo = [[-1] * n for _ in range(m)]
        def dp(i, j):
            if i == m - 1 and j == n - 1:
                return 1 if dungeon[i][j] >= 0 else 1 - dungeon[i][j]
            
            if i == m or j == n:
                return math.inf
            
            if memo[i][j] != -1: return memo[i][j]
            
            res = min(dp(i + 1, j), dp(i, j + 1)) - dungeon[i][j]
            memo[i][j] = 1 if res <= 0 else res
            return memo[i][j]
        
        return dp(0, 0)

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m = len(dungeon)
        n = len(dungeon[0])
        
        dp = [[0] * n for _ in range(m)]
        
        dp[m - 1][n - 1] = 1 if dungeon[-1][-1] >= 0 else 1 - dungeon[-1][-1]
        
        for i in range(m - 2, -1, -1):
            res = dp[i + 1][n - 1] - dungeon[i][n - 1]
            dp[i][n - 1] = 1 if res <= 0 else res
        
        for j in range(n - 2, -1, -1):
            res = dp[m - 1][j + 1] - dungeon[m - 1][j]
            dp[m - 1][j] = 1 if res <= 0 else res

        
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                res = min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j]
                dp[i][j] = 1 if res <= 0 else res
        
        return dp[0][0]