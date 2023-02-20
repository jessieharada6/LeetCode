class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # @cache
        # def dfs(row, col) -> int:
        #     if row < 0 or col < 0: return 0
        #     if row == 0 and col == 0: return 1
        #     return dfs(row - 1, col) + dfs(row, col - 1)
        # return dfs(m - 1, n - 1)

        # f = [[0] * (n) for _ in range(m)]
        # f[0][0] = 1
        # for row in range(m):
        #     for col in range(n):
        #         if row == 0 and col == 0: continue
        #         a = f[row - 1][col] if row - 1 >= 0 else 0
        #         b = f[row][col - 1] if col - 1 >= 0 else 0
        #         f[row][col] = a + b
        # return f[-1][-1]

        f = [0] * n
        f[0] = 1
        for row in range(m):
            for col in range(n):
                a = f[col]
                b = f[col - 1] if col - 1 >= 0 else 0
                f[col] = a + b
        return f[-1]