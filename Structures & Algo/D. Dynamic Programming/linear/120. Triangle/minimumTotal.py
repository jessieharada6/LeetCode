# 从上到下 - 只有一个入口
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        # @cache
        # def dfs(row, col) -> int:
        #     if row >= n or col >= n or col > row: return 0

        #     return triangle[row][col] + min(dfs(row + 1, col), dfs(row + 1, col + 1))
        # return dfs(0, 0)

        # f = [[0] * (r + 1) for r in range(n)]
        # for col in range(n): f[n - 1][col] = triangle[n - 1][col]
        # for r in range(n - 2, -1, -1):
        #     for c in range(r + 1):
        #         a = f[r + 1][c] if c < n and c <= r + 1 else inf
        #         b = f[r + 1][c + 1] if c + 1 < n and c + 1 <= r + 1 else inf
        #         f[r][c] = triangle[r][c] + min(a, b)

        # return f[0][0]

        f = [0] * n
        for col in range(n): f[col] = triangle[n - 1][col]
        for r in range(n - 2, -1, -1):
            for c in range(r + 1):
                a = f[c] if c < n else inf
                b = f[c + 1] if c + 1 < n else inf
                f[c] = triangle[r][c] + min(a, b)

        return f[0]

# 从下面往上 - 由多个入口
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        # @cache
        # def dfs(row, col) -> int:
        #     if row < 0 or col < 0 or col > row: return inf
        #     if row == 0: return triangle[0][0]  # and col == 0

        #     return triangle[row][col] + min(dfs(row - 1, col), dfs(row - 1, col - 1))
        # return min(dfs(n - 1, i) for i in range(n)) i标记不同的终点 vs. Q64唯一的终点

        # f = [[0] * (r + 1) for r in range(n)] 是否初始化为inf更好 - 没关系，因为只有f[0][0]会被用到
        # f[0][0] = triangle[0][0]
        # for r in range(1, n):
        #     for c in range(r + 1):
        #         a = f[r - 1][c] if c >= 0 and c <= r - 1 else inf
        #         b = f[r - 1][c - 1] if c - 1 >= 0 and c - 1 <= r - 1 else inf
        #         cur = triangle[r][c]
        #         f[r][c] = cur + min(a, b)
        # return min(x for x in f[n - 1])

        f = [inf] * n
        f[0] = triangle[0][0]
        a, b = inf, inf
        for r in range(1, n):
            for c in range(r, -1, -1):
                a = f[c] if c >= 0 else inf
                b = f[c - 1] if c - 1 >= 0 else inf
                cur = triangle[r][c]
                f[c] = cur + min(a, b)
        return min(f)
