
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp_i_1 = 0
        dp_i_2 = 0
        
        for i in range(n - 1, -1, -1):
            dp_i = max(dp_i_1, dp_i_2 + nums[i])
            dp_i_2 = dp_i_1
            dp_i_1 = dp_i
        
        return dp_i
            
            
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [-1] * n
        
        def dp(nums, start):
            if start >= n:
                return 0
            
            if memo[start] != -1:
                return memo[start]
            
            memo[start] = max(dp(nums, start + 1), nums[start] + dp(nums, start + 2))
            return memo[start]
        
        return dp(nums, 0)



class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        
        for i in range(1, n):
            if i - 2 == -1:
                dp[i] = max(dp[i - 1], nums[i])
                continue
                
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])

        
        return dp[n - 1]