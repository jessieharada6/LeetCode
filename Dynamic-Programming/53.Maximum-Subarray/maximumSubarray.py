class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_max = nums[0]
        output = nums[0]
        
        for i in range(1, len(nums)):
            cur_max = max(nums[i], nums[i] + cur_max)
            output = max(output, cur_max)
        
        
        return output