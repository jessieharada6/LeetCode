class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        n = len(nums)
        def getAverage(l, r):
            return sum(nums[l: r + 1]) / (r - l + 1)

        @cache
        def dfs(left, k):
            if k == 1: return getAverage(left, n - 1)
            return max(getAverage(left, nextLeft - 1) + dfs(nextLeft, k - 1) for nextLeft in range(left + 1, n - k + 2))
        
        return dfs(0, k)
