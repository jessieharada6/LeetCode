class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        dp = [0 for _ in range(n)]
        dp[0] = 1
        
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                elif j > 0:
                    dp[j] += dp[j - 1]
        
        return dp[-1]

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid[0])
        n = len(obstacleGrid)
        dp = [0 for _ in range(m)]
        # if we make it 1 will also work 
        # because in the for loops below, we will check again
        # when if obstacleGrid[i][j] == 1:
        dp[0] = 1 if obstacleGrid[0][0] == 0 else 1
        
        for i in range(n):
            for j in range(m):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                else:
                    if j - 1 >= 0:
                        dp[j] += dp[j - 1]
        
        return dp[-1]