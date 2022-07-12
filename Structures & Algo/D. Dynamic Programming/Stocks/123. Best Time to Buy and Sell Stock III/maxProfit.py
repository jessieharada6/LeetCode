class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_k = 2
        n = len(prices)
        dp = [[[0] * 2 for _ in range(max_k + 1)] for _ in range(n)]

        for i in range(n):
            for k in range(max_k, 0, -1):
                if i - 1 == -1:
                    dp[i][k][0] = 0
                    dp[i][k][1] = -prices[i]
                    continue
                
                dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])
                dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i])
        
        return dp[n - 1][max_k][0]

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp_i10 = 0
        dp_i20 = 0
        dp_i11 = -math.inf
        dp_i21 = -math.inf

        for i in range(n):
            dp_i10 = max(dp_i10, dp_i11 + prices[i])
            dp_i11 = max(dp_i11, -prices[i])
            dp_i20 = max(dp_i20, dp_i21 + prices[i])
            dp_i21 = max(dp_i21, dp_i10 - prices[i])
        
        return dp_i20
                