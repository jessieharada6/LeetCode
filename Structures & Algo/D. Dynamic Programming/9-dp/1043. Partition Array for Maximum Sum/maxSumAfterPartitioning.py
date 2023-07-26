class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        # @cache
        # def dfs(i):
        #     #if i < 0: return 0

        #     res = curMax = 0
        #     for j in range(i, max(i - k, -1), -1):
        #         curMax = max(curMax, arr[j])
        #         res = max(res, dfs(j - 1) + curMax * (i - j + 1))
        #     return res
        
        # return dfs(n - 1)

        f = [0] * n
        for i in range(n):
            res = curMax = 0
            for j in range(i, max(i - k, -1), -1):
                curMax = max(curMax, arr[j])
                res = max(res, f[j - 1] + curMax * (i - j + 1))
            f[i] = res

        return f[-1]
    

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        @cache
        def dfs(i):
            if i == n: return 0
            res = -inf
            cur = 0
            for j in range(i, min(i + k, n)):
                cur = max(cur, arr[j])
                res = max(res, dfs(j + 1) + cur *(j - i + 1))
            return res
        return dfs(0)