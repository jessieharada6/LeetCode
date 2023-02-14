## def dfs(start, s) -> int
## 已选的硬币与待选的硬币的和是否等于amount，返回方式的总数
# 1. 
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        @cache
        def dfs(start, s) -> int:
            if s == amount: return 1
            if s > amount or start == n: return 0

            return dfs(start, s + coins[start]) + dfs(start + 1, s)
        
        return dfs(0, 0)

# 2. 
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        
        # cache[start][s]
        # start: [0, n - 1]
        # s: [0, amount - 1]
        cache = [[-1] * amount for _ in range(n)]
        def dfs(start, s) -> int:
            if s == amount: return 1
            if s > amount or start == n: return 0
            if cache[start][s] != -1: return cache[start][s]

            res = dfs(start, s + coins[start]) + dfs(start + 1, s)
            cache[start][s] = res
            return res
        
        return dfs(0, 0)

## def dfs(start, left) -> int:
## 待选的硬币的和是否可以等于left，返回方式的总数
# 3. 
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        
        @cache
        def dfs(start, left) -> int:
            if left == 0: return 1
            if left < 0 or start == 0: return 0
            
            return dfs(start, left - coins[start - 1]) + dfs(start - 1, left)
        
        return dfs(n, amount)

# 4. 记忆化搜索
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        
        # cache[start][s]
        # start: [0, n]
        # s: [0, amount]
        cache = [[-1] * (amount + 1) for _ in range(n + 1)]

        def dfs(start, left) -> int:
            if left == 0: return 1
            if left < 0 or start == 0: return 0

            if cache[start][left] != -1: return cache[start][left]
            
            res = dfs(start, left - coins[start - 1]) + dfs(start - 1, left)
            cache[start][left] = res
            return res
        
        return dfs(n, amount)

# 5. 递推
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        
        f = [[0] * (amount + 1) for _ in range(n + 1)]
        for start in range(n + 1): f[start][0] = 1 #剩下的是0，还没开始选硬币。所以有1种选法-不选
        for start in range(1, n + 1):
            for left in range(1, amount + 1):
                if left - coins[start - 1] >= 0:
                    f[start][left] = f[start][left - coins[start - 1]] + f[start - 1][left]
                else:
                    f[start][left] = f[start - 1][left] #当前这枚硬币面值太大，不选
        return f[start][amount]
 
 # 6. 两个数组
 class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        
        f = [[0] * (amount + 1) for _ in range(2)]
        for start in range(2): f[start][0] = 1   # if left == 0: return 1
        for start in range(1, n + 1):
            for left in range(1, amount + 1):
                if left - coins[start - 1] >= 0:
                    f[start % 2][left] = f[start % 2][left - coins[start - 1]] + f[(start - 1) % 2][left]
                else:
                    f[start % 2][left] = f[(start - 1) % 2][left] 
        return f[n % 2][amount]
 
 # 7. 一维dp
 class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        
        f = [0] * (amount + 1)
        f[0] = 1 
        for start in range(1, n + 1):
            x = coins[start - 1]
            for left in range(x, amount + 1):
                f[left] += f[left - x] 

        return f[amount]
 