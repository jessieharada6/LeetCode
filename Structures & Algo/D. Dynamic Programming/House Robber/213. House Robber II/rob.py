class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        def dp(nums, start, end):
            dp_i_1 = 0
            dp_i_2 = 0
            
            for i in range(end - 1, start - 1, -1):
                dp_i = max(dp_i_1, dp_i_2 + nums[i])
                dp_i_2 = dp_i_1
                dp_i_1 = dp_i
            
            return dp_i
        
        return max(dp(nums, 0, n - 1), dp(nums, 1, n))