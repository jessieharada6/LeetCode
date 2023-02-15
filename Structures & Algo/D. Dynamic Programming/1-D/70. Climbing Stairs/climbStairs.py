class Solution:
    def climbStairs(self, n: int) -> int:
        # @cache
        # def dfs(steps):
        #     if steps == 0 or steps == 1: return 1  
        #     return dfs(steps - 1) + dfs(steps - 2)

        # return dfs(n)

        # f = [0] * (n + 1)
        # f[0] = 1 # 第0步
        # f[1] = 1 # 第一步
        # for i in range(2, n + 1):
        #     f[i] = f[i - 1] + f[i - 2]

        # return f[n]
        
        a, b = 1, 1 
        for i in range(2, n + 1):
            a, b = b, a + b
        return b 
        
###
class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def dfs(steps) -> int:
            if steps == 0: return 1
            if steps < 0: return 0

            return dfs(steps - 1) + dfs(steps - 2)
        return dfs(n)

class Solution:
    def climbStairs(self, n: int) -> int:
        f = [0] * (n + 2)
        f[1] = 1

        for steps in range(2, n + 2):
            f[steps] = f[steps - 1] + f[steps - 2]
        return f[-1]

class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 0, 1
        for x in range(n):
            a, b = b, a + b
        return b

###########
# 3. 
class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {0: 1, 1: 1}
        ways = 0
        for i in range(2, n + 1):
            ways = cache[i - 1] + cache[i - 2]
            cache[i] = ways
        return cache[n]

# 4. 
class Solution:
    def climbStairs(self, n: int) -> int:
        ans = 0
        cache = {0:1, 1: 1}

        def dfs(n):
            nonlocal ans
            if n < 0: 
                return 0

            if n in cache:
                return cache[n]
            
            ans = dfs(n - 1) + dfs(n - 2)
            cache[n] = ans
            return ans
        
        dfs(n + 1)
        return cache[n]

# 6. 
class Solution:
    def climbStairs(self, n: int) -> int:
        f = [1] * (n + 1)
        
        ways = 0
        for i in range(2, n + 1):
            ways = f[i - 1] + f[i - 2]
            f[i] = ways

        return f[n]

# 7. 
class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1
        for i in range(2, n + 1):
            b, a = a + b, b

        return b

# 9.
class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}

        def dfs(n):
            if n < 0: return 0
            if n in cache: return cache[n]
            if n == 0 or n == 1: return 1

            ans = dfs(n - 1) + dfs(n - 2)

            cache[n] = ans
            return ans
        
        return dfs(n)


### 超时/错误/不必要
#2. 错误的 - STEPS = 1 返回的是0? 因为ans=0在外面没有被赋值 dfs(1)返回的是1

# 1. 我不会转成cache？
class Solution:
    def climbStairs(self, n: int) -> int:
        ans = 0
        cache = {}

        def dfs(steps):
            nonlocal ans
            if steps > n: 
                return
            if steps == n: 
                ans += 1
                return
            
            dfs(steps + 1)
            dfs(steps + 2)
        
        dfs(0)
        return ans

class Solution:
    def climbStairs(self, n: int) -> int:
        ans = 0
        cache = {}

        def dfs(n):
            nonlocal ans

            if n < 0: return 0
            if n in cache: return cache[n]
            if n == 1: return 1
            
            ans += dfs(n - 1)
            ans += dfs(n - 2)

            cache[n] = ans
            return ans
        
        dfs(n)
        return ans
# 5. 这个对了 为什么steps = 1 不能返回正确的？ 显而易见-if n == 1: return 1
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1

        ans = 0
        cache = {}
        
        def dfs(n):
            nonlocal ans
            if n < 0: 
                return 0
            
            if n in cache:
                return cache[n]
            
            if n == 0 or n == 1: return 1
            
            ans = dfs(n - 1) + dfs(n - 2)
            cache[n] = ans
            return ans
        
        dfs(n)
        return ans

# 8.
class Solution:
    def climbStairs(self, n: int) -> int:
        ans = 0 # 没必要 看9
        cache = {}

        def dfs(n):
            nonlocal ans
            if n < 0: 
                return 0
            
            if n in cache:
                return cache[n]
            
            if n == 0 or n == 1:
                return 1
            
            ans = dfs(n - 1) + dfs(n - 2)
            cache[n] = ans
            return ans
        
        return dfs(n)
