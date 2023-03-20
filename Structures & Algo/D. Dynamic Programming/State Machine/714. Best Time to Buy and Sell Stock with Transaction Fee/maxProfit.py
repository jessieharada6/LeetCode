class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        f = [[0] * 2 for _ in range(n)]
        f[0][0] = 0
        f[0][1] = -prices[0]
        for i in range(1, n):
            f[i][0] = max(f[i - 1][0], f[i - 1][1] + prices[i] - fee) # 卖是有手续费
            f[i][1] = max(f[i - 1][1], f[i - 1][0] - prices[i])
        return f[n - 1][0]

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        f = [[0] * 2 for _ in range(n + 1)]
        f[0][1] = -math.inf

        for i in range(1, n + 1):
            f[i][1] = max(f[i - 1][True], f[i - 1][False] - prices[i - 1])
            f[i][0] = max(f[i - 1][False], f[i - 1][True] + prices[i - 1] - fee)

        return f[n][False]
    

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        f = [[0] * 2 for _ in range(n + 2)]
        f[0][1] = -math.inf
        
        for i, p in enumerate(prices):
            f[i + 1][1] = max(f[i][True], f[i][False] - p)
            f[i + 1][0] = max(f[i][False], f[i][True] + p - fee)

        return f[n][False]