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

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0 for _ in range(amount + 1)]
        dp[0] = 1
        
        for coin in coins:
            for i in range(amount + 1):
                if i - coin >= 0:
                    dp[i] = dp[i - coin] + dp[i]
        
        return dp[-1]