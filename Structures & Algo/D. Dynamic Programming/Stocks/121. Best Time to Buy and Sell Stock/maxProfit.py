class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        
        dp_i_0 = 0
        dp_i_1 = -math.inf
        
        for i in range(n):
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, -prices[i])
        
        return dp_i_0


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        
        dp = [[0] * 2 for _ in range(n)]
        
        print(dp)
        for i in range(n):
            if i - 1 == -1:
                dp[i][0] = 0
                dp[i][1] = -prices[i] # dp[-1][1] = -math.inf, dp[-1][0] - prices[i] = -prices[i]
                continue
            
            print("yesterday", dp[i - 1][0], dp[i - 1][1])
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], -prices[i])
            print("today", dp[i][0], dp[i][1])
        
        return dp[n - 1][0]