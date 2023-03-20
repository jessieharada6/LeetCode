class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        f = [[[0] * 2 for _ in range(2 + 1)] for _ in range(n + 1)]
        for j in range(2 + 1):
            f[0][j][1] = -math.inf
        

        for i in range(1, n + 1):
            for j in range(2 + 1):
                f[i][j][0] = max(f[i - 1][j][0], f[i - 1][j][1] + prices[i - 1])
                f[i][j][1] = max(f[i - 1][j][1], f[i - 1][j - 1][0] - prices[i - 1]) if j else f[i - 1][j][1]

        return f[n][2][0]