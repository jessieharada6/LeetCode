class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        #以i为结尾的 长度最多是k的 max val sum
        @cache
        def dfs(i):
            if i < 0: return 0

            curMax, res = 0, 0
            for j in range(i, max(i - k, -1), -1):
                curMax = max(arr[j], curMax)
                res = max(res, dfs(j - 1) + curMax * (i - j + 1))
            return res

        return dfs(n - 1)
        
    # 每个子数组长度至少是 k, the rest remains the same - greedy - get max val of the arr * (len(arr) - 1)

    # 每个子数组长度至少是 k，数组元素都改成最小值
    # 求的仍然是最大值
    # cur = min(cur, arr[j]) the rest is the same, keep all values at length of k



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