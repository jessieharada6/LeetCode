class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # @cache
        # def dfs(row, col) -> int:
        #     if row < 0 or col < 0: return inf
        #     if row == 0 and col == 0: return grid[0][0]
        #     return grid[row][col] + min(dfs(row - 1, col), dfs(row, col - 1))
        # return dfs(m - 1, n - 1)

        # f = [[inf] * n for _ in range(m)]
        # f[0][0] = grid[0][0]
        ## a, b = inf, inf 无需declare
        # for row in range(m):
        #     for col in range(n):
        #         if row == 0 and col == 0: continue
        #         a = f[row - 1][col] if row - 1 >= 0 else inf
        #         b = f[row][col - 1] if col - 1 >= 0 else inf
        #         f[row][col] = grid[row][col] + min(a, b)

        # return f[-1][-1]

        f = [inf] * n
        f[0] = grid[0][0]
        for row in range(m):
            for col in range(n):
                if row == 0 and col == 0: continue
                a = f[col]
                b = f[col - 1] if col - 1 >= 0 else inf
                f[col] = grid[row][col] + min(a, b)

        return f[-1]