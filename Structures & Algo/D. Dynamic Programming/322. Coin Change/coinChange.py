class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [-666 for _ in range(amount + 1)]
        
        def dp(coins, amount):
            if amount == 0: return 0 
            if amount < 0: return -1
            
            if memo[amount] != -666:
                return memo[amount]
            
            res = math.inf
            for coin in coins:
                sub = dp(coins, amount - coin)
                if sub == -1: continue
                res = min(res, sub + 1)
            
            memo[amount] = res if res != math.inf else -1
            return memo[amount]
        
        return dp(coins, amount)

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1 for _ in range(amount + 1)]
        dp[0] = 0
        
        for i in range(1, len(dp)):
            for coin in coins:
                if i - coin < 0: continue
                dp[i] = min(dp[i], dp[i - coin] + 1)
        
        return dp[-1] if dp[-1] != amount + 1 else -1
            

