class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n

        dp_i_0 = 0
        dp_i_1 = 1
        dp_i = 0
        
        for i in range(2, n + 1):
            dp_i = dp_i_0 + dp_i_1
            dp_i_0 = dp_i_1
            dp_i_1 = dp_i

        return dp_i
        
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0

        dpTable = [0 for _ in range(n + 1)]
        dpTable[1] = 1
        
        for i in range(2, n + 1):
            dpTable[i] = dpTable[i - 1] + dpTable[i - 2]
        
        return dpTable[-1]

class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        
        if n == 1 or n == 2:
            return 1
        
        memo = defaultdict(int)
        if n in memo:
            return memo[n]

        # res = self.fib(n - 1) + self.fib(n - 2)
        # memo[n] = res
        # return res
        memo[n] = self.fib(n - 1) + self.fib(n - 2)
        return memo[n]

class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        
        if n == 1 or n == 2:
            return 1
        
        return self.fib(n - 1) + self.fib(n - 2)