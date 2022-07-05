class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0 for _ in range(n)]
        dp[0] = nums[0]
        
        for i in range(1, n):
            dp[i] = max(nums[i] + dp[i - 1], nums[i])

        return max(dp)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp_0 = nums[0]
        dp_1 = -math.inf
        dp = dp_0
        
        for i in range(1, n):
            dp_1 = max(nums[i] + dp_0, nums[i])
            dp_0 = dp_1
            dp = max(dp, dp_0)

        return dp