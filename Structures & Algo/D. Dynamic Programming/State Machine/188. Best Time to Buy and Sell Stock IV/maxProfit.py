class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        # @cache
        # def dfs(i, j, hold):
        #     if i == 0:
        #         return 0 if not hold else -math.inf

        #     if not hold:
        #         return max(dfs(i - 1, j, False), dfs(i - 1, j, True) + prices[i - 1])
        #     elif j:  # hold and j > 0
        #         return max(dfs(i - 1, j, True), dfs(i - 1, j - 1, False) - prices[i - 1])
        #     else:    # hold and j == 0
        #         return dfs(i - 1, j, True)
        
        # return dfs(n, k, False)

        f = [[[0] * 2 for _ in range(k + 1)] for _ in range(n + 1)]
        for j in range(k + 1):
            f[0][j][1] = -math.inf
        

        for i in range(1, n + 1):
            for j in range(k + 1):
                f[i][j][0] = max(f[i - 1][j][0], f[i - 1][j][1] + prices[i - 1])
                f[i][j][1] = max(f[i - 1][j][1], f[i - 1][j - 1][0] - prices[i - 1]) if j else f[i - 1][j][1]

        return f[n][k][0]

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        # @cache
        # def dfs(i, j, hold):
        #     if i < 0:
        #         return 0 if not hold else -math.inf

        #     if not hold:
        #         return max(dfs(i - 1, j, False), dfs(i - 1, j, True) + prices[i])
        #     elif j:  # hold and j > 0
        #         return max(dfs(i - 1, j, True), dfs(i - 1, j - 1, False) - prices[i])
        #     else:    # hold and j == 0
        #         return dfs(i - 1, j, True)
        
        # return dfs(n - 1, k, False)

        f = [[[0] * 2 for _ in range(k + 1)] for _ in range(n + 2)]
        for j in range(k + 1):
            f[0][j][1] = -math.inf
            f[1][j][1] = -math.inf

        for i, p in enumerate(prices):
            for j in range(k + 1):
                f[i + 2][j][0] = max(f[i + 1][j][0], f[i + 1][j][1] + p)
                f[i + 2][j][1] = max(f[i + 1][j][1], f[i + 1][j - 1][0] - p) if j else f[i + 1][j][1]

        return f[n + 1][k][0]