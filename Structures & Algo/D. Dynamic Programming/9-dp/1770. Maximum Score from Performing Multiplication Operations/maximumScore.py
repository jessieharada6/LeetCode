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
        @cache
        def dfs(l, r):
            i = n - 1 - r + l
            if i == m: return 0

            res1 = nums[l] * multipliers[i] + dfs(l + 1, r)
            res2 = nums[r] * multipliers[i] + dfs(l, r - 1)

            return max(res1, res2)
        return dfs(0, n - 1)