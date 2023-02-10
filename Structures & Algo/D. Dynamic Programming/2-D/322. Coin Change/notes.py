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
            

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [-666 for _ in range(amount + 1)]
        
        def dp(coins, amount):
            if amount == 0:
                print("=", amount)
                return 0
            
            if amount < 0:
                print("<", amount)
                return -1
            
            res = math.inf
            
            if memo[amount] != -666:
                print("memo amount", memo, amount)
                return memo[amount]
            
            print(amount)
            for coin in coins:
                print("sub-amount", amount, coin, res, amount - coin)
                sub = dp(coins, amount - coin)
                print("sub", sub, memo)
                if sub == -1: 
                    print("subsub", sub)
                    continue
                res = min(res, sub + 1)
                print("res", res, sub + 1)
            
            memo[amount] = res if res != math.inf else -1
            print("memo", memo, res)
            return memo[amount]
        
        dp(coins, amount)
        print(memo)


# 3
# sub 3 2 inf 1
# 1
# sub 1 2 inf -1
# < -1
# sub -1 [-666, -666, -666, -666]
# subsub -1
# memo [-666, -1, -666, -666] inf
# sub -1 [-666, -1, -666, -666]                 --- as when amount is 1, memo[amount] = -1, so when 3 - 2 it is also -1, as this is the purpose of memo  
# subsub -1
# memo [-666, -1, -666, -1] inf
# [-666, -1, -666, -1]



# 11
# sub-amount 11 1 inf 10
# 10
# sub-amount 10 1 inf 9
# 9
# sub-amount 9 1 inf 8
# 8
# sub-amount 8 1 inf 7
# 7
# sub-amount 7 1 inf 6
# 6
# sub-amount 6 1 inf 5
# 5
# sub-amount 5 1 inf 4
# 4
# sub-amount 4 1 inf 3
# 3
# sub-amount 3 1 inf 2
# 2
# sub-amount 2 1 inf 1
# 1
# sub-amount 1 1 inf 0
# = 0
# sub 0 [-666, -666, -666, -666, -666, -666, -666, -666, -666, -666, -666, -666]
# res 1 1
# sub-amount 1 2 1 -1
# < -1
# sub -1 [-666, -666, -666, -666, -666, -666, -666, -666, -666, -666, -666, -666]
# subsub -1
# sub-amount 1 5 1 -4
# < -4
# sub -1 [-666, -666, -666, -666, -666, -666, -666, -666, -666, -666, -666, -666]
# subsub -1
# memo [-666, 1, -666, -666, -666, -666, -666, -666, -666, -666, -666, -666] 1
# sub 1 [-666, 1, -666, -666, -666, -666, -666, -666, -666, -666, -666, -666]
# res 2 2
# sub-amount 2 2 2 0
# = 0
# sub 0 [-666, 1, -666, -666, -666, -666, -666, -666, -666, -666, -666, -666]
# res 1 1
# sub-amount 2 5 1 -3
# < -3
# sub -1 [-666, 1, -666, -666, -666, -666, -666, -666, -666, -666, -666, -666]
# subsub -1
# memo [-666, 1, 1, -666, -666, -666, -666, -666, -666, -666, -666, -666] 1
# sub 1 [-666, 1, 1, -666, -666, -666, -666, -666, -666, -666, -666, -666]
# res 2 2
# sub-amount 3 2 2 1
# memo amount [-666, 1, 1, -666, -666, -666, -666, -666, -666, -666, -666, -666] 1
# sub 1 [-666, 1, 1, -666, -666, -666, -666, -666, -666, -666, -666, -666]
# res 2 2
# sub-amount 3 5 2 -2
# < -2
# sub -1 [-666, 1, 1, -666, -666, -666, -666, -666, -666, -666, -666, -666]
# subsub -1
# memo [-666, 1, 1, 2, -666, -666, -666, -666, -666, -666, -666, -666] 2
# sub 2 [-666, 1, 1, 2, -666, -666, -666, -666, -666, -666, -666, -666]
# res 3 3
# sub-amount 4 2 3 2
# memo amount [-666, 1, 1, 2, -666, -666, -666, -666, -666, -666, -666, -666] 2
# sub 1 [-666, 1, 1, 2, -666, -666, -666, -666, -666, -666, -666, -666]
# res 2 2
# sub-amount 4 5 2 -1
# < -1
# sub -1 [-666, 1, 1, 2, -666, -666, -666, -666, -666, -666, -666, -666]
# subsub -1
# memo [-666, 1, 1, 2, 2, -666, -666, -666, -666, -666, -666, -666] 2
# sub 2 [-666, 1, 1, 2, 2, -666, -666, -666, -666, -666, -666, -666]
# res 3 3
# sub-amount 5 2 3 3
# memo amount [-666, 1, 1, 2, 2, -666, -666, -666, -666, -666, -666, -666] 3
# sub 2 [-666, 1, 1, 2, 2, -666, -666, -666, -666, -666, -666, -666]
# res 3 3
# sub-amount 5 5 3 0
# = 0
# sub 0 [-666, 1, 1, 2, 2, -666, -666, -666, -666, -666, -666, -666]
# res 1 1
# memo [-666, 1, 1, 2, 2, 1, -666, -666, -666, -666, -666, -666] 1
# sub 1 [-666, 1, 1, 2, 2, 1, -666, -666, -666, -666, -666, -666]
# res 2 2
# sub-amount 6 2 2 4
# memo amount [-666, 1, 1, 2, 2, 1, -666, -666, -666, -666, -666, -666] 4
# sub 2 [-666, 1, 1, 2, 2, 1, -666, -666, -666, -666, -666, -666]
# res 2 3
# sub-amount 6 5 2 1
# memo amount [-666, 1, 1, 2, 2, 1, -666, -666, -666, -666, -666, -666] 1
# sub 1 [-666, 1, 1, 2, 2, 1, -666, -666, -666, -666, -666, -666]
# res 2 2
# memo [-666, 1, 1, 2, 2, 1, 2, -666, -666, -666, -666, -666] 2
# sub 2 [-666, 1, 1, 2, 2, 1, 2, -666, -666, -666, -666, -666]
# res 3 3
# sub-amount 7 2 3 5
# memo amount [-666, 1, 1, 2, 2, 1, 2, -666, -666, -666, -666, -666] 5
# sub 1 [-666, 1, 1, 2, 2, 1, 2, -666, -666, -666, -666, -666]
# res 2 2
# sub-amount 7 5 2 2
# memo amount [-666, 1, 1, 2, 2, 1, 2, -666, -666, -666, -666, -666] 2
# sub 1 [-666, 1, 1, 2, 2, 1, 2, -666, -666, -666, -666, -666]
# res 2 2
# memo [-666, 1, 1, 2, 2, 1, 2, 2, -666, -666, -666, -666] 2
# sub 2 [-666, 1, 1, 2, 2, 1, 2, 2, -666, -666, -666, -666]
# res 3 3
# sub-amount 8 2 3 6
# memo amount [-666, 1, 1, 2, 2, 1, 2, 2, -666, -666, -666, -666] 6
# sub 2 [-666, 1, 1, 2, 2, 1, 2, 2, -666, -666, -666, -666]
# res 3 3
# sub-amount 8 5 3 3
# memo amount [-666, 1, 1, 2, 2, 1, 2, 2, -666, -666, -666, -666] 3
# sub 2 [-666, 1, 1, 2, 2, 1, 2, 2, -666, -666, -666, -666]
# res 3 3
# memo [-666, 1, 1, 2, 2, 1, 2, 2, 3, -666, -666, -666] 3
# sub 3 [-666, 1, 1, 2, 2, 1, 2, 2, 3, -666, -666, -666]
# res 4 4
# sub-amount 9 2 4 7
# memo amount [-666, 1, 1, 2, 2, 1, 2, 2, 3, -666, -666, -666] 7
# sub 2 [-666, 1, 1, 2, 2, 1, 2, 2, 3, -666, -666, -666]
# res 3 3
# sub-amount 9 5 3 4
# memo amount [-666, 1, 1, 2, 2, 1, 2, 2, 3, -666, -666, -666] 4
# sub 2 [-666, 1, 1, 2, 2, 1, 2, 2, 3, -666, -666, -666]
# res 3 3
# memo [-666, 1, 1, 2, 2, 1, 2, 2, 3, 3, -666, -666] 3
# sub 3 [-666, 1, 1, 2, 2, 1, 2, 2, 3, 3, -666, -666]
# res 4 4
# sub-amount 10 2 4 8
# memo amount [-666, 1, 1, 2, 2, 1, 2, 2, 3, 3, -666, -666] 8
# sub 3 [-666, 1, 1, 2, 2, 1, 2, 2, 3, 3, -666, -666]
# res 4 4
# sub-amount 10 5 4 5
# memo amount [-666, 1, 1, 2, 2, 1, 2, 2, 3, 3, -666, -666] 5
# sub 1 [-666, 1, 1, 2, 2, 1, 2, 2, 3, 3, -666, -666]
# res 2 2
# memo [-666, 1, 1, 2, 2, 1, 2, 2, 3, 3, 2, -666] 2
# sub 2 [-666, 1, 1, 2, 2, 1, 2, 2, 3, 3, 2, -666]
# res 3 3
# sub-amount 11 2 3 9
# memo amount [-666, 1, 1, 2, 2, 1, 2, 2, 3, 3, 2, -666] 9
# sub 3 [-666, 1, 1, 2, 2, 1, 2, 2, 3, 3, 2, -666]
# res 3 4
# sub-amount 11 5 3 6
# memo amount [-666, 1, 1, 2, 2, 1, 2, 2, 3, 3, 2, -666] 6
# sub 2 [-666, 1, 1, 2, 2, 1, 2, 2, 3, 3, 2, -666]
# res 3 3
# memo [-666, 1, 1, 2, 2, 1, 2, 2, 3, 3, 2, 3] 3
# [-666, 1, 1, 2, 2, 1, 2, 2, 3, 3, 2, 3]
