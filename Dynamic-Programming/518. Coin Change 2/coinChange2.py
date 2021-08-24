class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = amount + 1
        dp = [0 for _ in range(n)]
        dp[0] = 1
        
        for coin in coins:
            for currency in range(n):
                if currency - coin >= 0:
                    dp[currency] = dp[currency] + dp[currency - coin]
        
        return dp[-1]            