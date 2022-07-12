class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        
        dp_i_0 = 0
        dp_i_1 = -math.inf
        dp_pre_0 = 0      # dp[i - 2][0]
        
        
        for i in range(n):
            yesterday_no_stock = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, dp_pre_0 - prices[i])
            dp_pre_0 = yesterday_no_stock
        
        return dp_i_0


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * 2 for _ in range(n)]
        
        for i in range(n):
            if i - 1 == -1:
                dp[i][0] = 0
                dp[i][1] = -prices[i]
                continue
            
            if i - 1 == -2:
                dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
                # dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
                dp[i][1] = max(dp[i - 1][1], -prices[i])
                continue
            
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - prices[i])
        
        return dp[n - 1][0]