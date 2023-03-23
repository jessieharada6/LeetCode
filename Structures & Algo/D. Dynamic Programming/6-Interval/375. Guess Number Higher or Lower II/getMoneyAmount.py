class Solution:
    def getMoneyAmount(self, n: int) -> int:
        # @cache
        # def dfs(left, right):
        #     if right <= left: return 0       # right - left + 1 <= 1

        #     res = inf
        #     for i in range(left, right + 1): # dynamic bounds
        #         # 有可能left == i - 1 or left > i - 1 (i - 1 = right) 要维护
        #         cur = i + max(dfs(left, i - 1)  , dfs(i + 1, right))
        #         res = min(cur, res)

        #     return res
        # return dfs(1, n)

        # f = [[0] * (n + 1) for _ in range(n + 2)]
        # for left in range(n + 1, 0, -1):
        #     for right in range(left + 1, n + 1):
        #         res = inf
        #         for i in range(left, right + 1): 
        #             res1= f[left][i - 1]
        #             res2 =f[i + 1][right] 
        #             cur = i + max( res1,res2 )
        #             res = min(cur, res)
        #         f[left][right] = res
        # return f[1][n]

        f = [[0] * (n + 1) for _ in range(n + 1)]
        for left in range(n, 0, -1):
            for right in range(left + 1, n + 1):
                res = inf
                for i in range(left, right + 1): 
                    res1= f[left][i - 1] 
                    res2 =f[i + 1][right]  if i < right else 0
                    cur = i + max( res1,res2 )
                    res = min(cur, res)
                f[left][right] = res
        return f[1][n]





    
#print(Solution().getMoneyAmount(n = 5))
