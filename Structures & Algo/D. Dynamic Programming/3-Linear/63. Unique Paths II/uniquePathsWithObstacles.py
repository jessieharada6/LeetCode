class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        # @cache
        # def dfs(row, col) -> int:
        #     # obstacleGrid[row][col] == 1包含了当obstacleGrid[0][0] == 1的情况
        #     if row < 0 or col < 0 or obstacleGrid[row][col] == 1: return 0
        #     if row == 0 and col == 0: return 1
        #     return dfs(row - 1, col) + dfs(row, col - 1)
        
        # return dfs(m - 1, n - 1)

        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
        # f = [[0] * (n) for _ in range(m)]
        # f[0][0] = 1
        # for row in range(m):
        #     for col in range(n):
        #         if row == 0 and col == 0: continue
        #         a = f[row - 1][col] if row - 1 >= 0 and obstacleGrid[row - 1][col] != 1 else 0
        #         b = f[row][col - 1] if col - 1 >= 0 and obstacleGrid[row][col - 1] != 1 else 0
        #         f[row][col] = a + b
        # return f[-1][-1]

        f = [0] * n
        f[0] = 1
        for row in range(m):
            for col in range(n):
                if row == 0 and col == 0: continue
                a = f[col] if row - 1 >= 0 and obstacleGrid[row - 1][col] != 1 else 0
                b = f[col - 1] if col - 1 >= 0 and obstacleGrid[row][col - 1] != 1 else 0
                f[col] = a + b
        return f[-1]
