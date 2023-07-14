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