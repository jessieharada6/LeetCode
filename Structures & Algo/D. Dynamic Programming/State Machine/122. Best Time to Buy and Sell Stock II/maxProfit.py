class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        # @cache
        # def dfs(i, hold):
        #     if i == n: return 0

        #     if not hold:
        #         return max(dfs(i + 1, False), dfs(i + 1, True) - prices[i])
        #     else:
        #         return max(dfs(i + 1, True), dfs(i + 1, False) + prices[i])
        # return dfs(0, False)

        # @cache
        # def dfs(i, hold):
        #     if i == 0 and not hold: return 0
        #     if i == 0 and hold: return -prices[0]

        #     if not hold:
        #         return max(dfs(i - 1, False), dfs(i - 1, True) + prices[i])
        #     else:
        #         return max(dfs(i - 1, True), dfs(i - 1, False) - prices[i])
        # return dfs(n - 1, False)

        f = [[0] * 2 for _ in range(n)]
        f[0][0] = 0
        f[0][1] = -prices[0]
        for i in range(1, n):
            f[i][0] = max(f[i - 1][0], f[i - 1][1] + prices[i])
            f[i][1] = max(f[i - 1][1], f[i - 1][0] - prices[i])
        return f[n - 1][0]
    

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        # @cache
        # def dfs(i, hold):
        #     if i == 0:
        #         return 0 if not hold else -math.inf

        #     if hold:
        #         return max(dfs(i - 1, True), dfs(i - 1, False) - prices[i - 1])
        #     else:
        #         return max(dfs(i - 1, False), dfs(i - 1, True) + prices[i - 1])
        
        # return dfs(n, False)

        # f = [[0] * 2 for _ in range(n + 1)]
        # f[0][1] = -math.inf

        # for i in range(1, n + 1):
        #     f[i][1] = max(f[i - 1][True], f[i - 1][False] - prices[i - 1])
        #     f[i][0] = max(f[i - 1][False], f[i - 1][True] + prices[i - 1])

        # return f[n][False]

        # @cache
        # def dfs(i, hold):
        #     if i < 0:
        #         return 0 if not hold else -math.inf

        #     if hold:
        #         return max(dfs(i - 1, True), dfs(i - 1, False) - prices[i])
        #     else:
        #         return max(dfs(i - 1, False), dfs(i - 1, True) + prices[i])
        
        # return dfs(n - 1, False)
    
        f = [[0] * 2 for _ in range(n + 2)]
        f[0][1] = -math.inf
        
        for i, p in enumerate(prices):
            f[i + 1][1] = max(f[i][True], f[i][False] - p)
            f[i + 1][0] = max(f[i][False], f[i][True] + p)

        return f[n][False]