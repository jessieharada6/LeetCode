# backtracking leads to Time Limit Exceeded
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        paths = []
        
        def traverse(path):
            if sum(path) == amount:
                paths.append(path[:])
                return
            
            if sum(path) > amount:
                return
            
            for i in range(len(coins)):
                path.append(coins[i])
                traverse(path)
                path.pop()
        
        traverse([])
        n = math.inf
        for p in paths:
            n = min(n, len(p))
        return n if n != math.inf else -1

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [math.inf for _ in range(amount + 1)]
        dp[0] = 0
        
        
        for i in range(len(dp)):
            for coin in coins:
                if i - coin < 0: continue
                dp[i] = min(dp[i], dp[i - coin] + 1)
        
        return dp[-1] if dp[-1] != math.inf else -1
            
             