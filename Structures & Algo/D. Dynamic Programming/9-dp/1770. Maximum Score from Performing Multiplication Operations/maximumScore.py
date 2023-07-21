class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n, m = len(nums), len(multipliers)
        @cache
        def dfs(l, r, i):
            if i == m: return 0

            res1 = nums[l] * multipliers[i] + dfs(l + 1, r, i + 1)
            res2 = nums[r] * multipliers[i] + dfs(l, r - 1, i + 1)

            return max(res1, res2)
        return dfs(0, n - 1, 0)
    
## O(m^2)

class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n, m = len(nums), len(multipliers)
        # @cache
        # def dfs(l, r):
        #     i = n - 1 - r + l
        #     if i == m: return 0

        #     return max(nums[l] * multipliers[i] + dfs(l + 1, r),
        #                nums[r] * multipliers[i] + dfs(l, r - 1))
        
        # return dfs(0, n - 1)

        if n > 2 * m:                   # maximum length of l to r
            nums = nums[:m] + nums[-m:] # nums becomes len(2m)
            n = 2 * m                   # update n
        f = [[0] * n for _ in range(m + 1)]
        for l in range(m - 1, -1, -1):
            for r in range(n - m, n):
                i = n - 1 - r + l
                if i >= m: continue
                f[l][r] = max(nums[l] * multipliers[i] + f[l + 1][r], nums[r] * multipliers[i] + f[l][r - 1])
        return f[0][n - 1]
        
        
class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n, m = len(nums), len(multipliers)
        # @cache
        # def dfs(l, r):
        #     i = n - 1 - r + l
        #     if i == m: return 0

        #     res1 = nums[l] * multipliers[i] + dfs(l + 1, r)
        #     res2 = nums[r] * multipliers[i] + dfs(l, r - 1)

        #     return max(res1, res2)
        # return dfs(0, n - 1)

        f = [[0] * (n) for _ in range(m + 1)]
        for l in range(m - 1, -1, -1): # for l in range(m - 1, 0, -1): stuck at here initially
            for r in range(n - m, n):
                i = n - 1 - r + l
                if i >= m: continue
                res1 = nums[l] * multipliers[i] + f[l + 1][r]
                res2 = nums[r] * multipliers[i] + f[l][r - 1]
                f[l][r] = max(res1, res2)
        return f[0][n - 1]