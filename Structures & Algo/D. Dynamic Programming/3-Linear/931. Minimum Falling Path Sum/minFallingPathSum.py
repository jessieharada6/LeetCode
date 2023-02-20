class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        # @cache
        # def dfs(row, col) -> int:
        #     if row < 0 or col < 0 or col >= m: return inf
        #     if row == 0: return matrix[0][col] #可以落在任意的first row
        #                                        #如果用if row == 0 and col == 0: return grid[0][0]表示只可以落在[0][0]点
        #     return matrix[row][col] + min(dfs(row - 1, col - 1), dfs(row - 1, col),  dfs(row - 1, col + 1))
        # return min(dfs(m - 1, i) for i in range(m))

        f = [[0] * m for _ in range(m)]
        for col in range(m): f[0][col] = matrix[0][col]
        for row in range(1, m):
            for col in range(m):
                a = f[row - 1][col - 1] if col - 1 >= 0 else inf
                b = f[row - 1][col]
                c = f[row - 1][col + 1] if col + 1 < m else inf
                f[row][col] = matrix[row][col] + min(a, b, c)
        return min(x for x in f[m - 1])