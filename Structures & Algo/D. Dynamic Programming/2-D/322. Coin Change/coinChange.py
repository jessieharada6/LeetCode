## def dfs(start, s) -> int 
## 已选的硬币和s与待选的硬币(>start)是否能够组成amount，如果可以并有多种方案，返回最少硬币数量
# 1. 
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        
        @cache
        def dfs(start, s) -> int:
            if s == amount: return 0 #触底 到达目标 归时-向上算
            if s > amount or start == n: return inf

            return min(dfs(start, s + coins[start]) + 1, dfs(start + 1, s))
        
        ans = dfs(0, 0) 
        return -1 if ans == inf else ans 

# 2. 
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        
        # cache[start][s]
        # start: [0, n - 1]
        # s: [0, amount - 1]
        cache = [[-1] * amount for _ in range(n)]
        def dfs(start, s) -> int:
            if s == amount: return 0 #触底 到达目标 归时-向上算
            if s > amount or start == n: return inf
            if cache[start][s] != -1: return cache[start][s]

            res = min(dfs(start, s + coins[start]) + 1, dfs(start + 1, s))
            cache[start][s] = res
            return res
        
        ans = dfs(0, 0) 
        return -1 if ans == inf else ans 

## def dfs(start, s) -> int:
## 可否在剩余组合中里找到和为left的硬币，如果有，返回最少硬币数量
# 3.
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        
        @cache
        def dfs(start, left) -> int:
            if left == 0: return 0 
            if left < 0 or start == 0: return inf

            return min(dfs(start, left - coins[start - 1]) + 1, dfs(start - 1, left))
        
        ans = dfs(n, amount) #也可以穿入n-1 但用cache不好操作
        return -1 if ans == inf else ans 

# 4. 记忆化搜索
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        
        # cache[start][left]
        # start: [0, n]
        # left: [0, amount]
        cache = [[-1] * (amount + 1) for _ in range(n + 1)]
        def dfs(start, left) -> int:
            if left == 0: return 0 
            if left < 0 or start == 0: return inf
            if cache[start][left] != -1: return cache[start][left]

            res = min(dfs(start, left - coins[start - 1]) + 1, dfs(start - 1, left))
            cache[start][left] = res
            return res
        
        ans = dfs(n, amount) 
        return -1 if ans == inf else ans 

# 5. 递推
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)

        f = [[inf] * (amount + 1) for _ in range(n + 1)]
        for start in range(n + 1): f[start][0] = 0
        for start in range(1, n + 1):
            for left in range(1, amount + 1):
                if left - coins[start - 1] >= 0:
                    f[start][left] = min(f[start][left - coins[start - 1]] + 1, f[start - 1][left])
                else:
                    f[start][left] = f[start - 1][left] # 如果<0 就不选这枚硬币
        
        return f[start][amount] if f[start][amount] != inf else -1
        # start已走到了n
        # return f[n][amount] if f[n][amount] != inf else -1

 # 6. 两个数组
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)

        f = [[inf] * (amount + 1) for _ in range(2)]
        for start in range(2): f[start][0] = 0    # if left == 0: return 0 
        for start in range(1, n + 1):
            for left in range(1, amount + 1):
                if left - coins[start - 1] >= 0:
                    f[start % 2][left] = min(f[start % 2][left - coins[start - 1]] + 1, f[(start - 1) % 2][left])
                else:
                    f[start % 2][left] = f[(start - 1) % 2][left] # 如果<0 就不选这枚硬币
        
        return f[n % 2][amount] if f[n % 2][amount] != inf else -1


# 7. 一维dp
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)

        f = [inf] * (amount + 1)
        f[0] = 0    

        for start in range(1, n + 1):
            x = coins[start - 1]
            for left in range(x, amount + 1):
                # if left >= coins[start - 1]:
                f[left] = min(f[left - x] + 1, f[left])
        
        return f[amount] if f[amount] != inf else -1













####################################
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
            

