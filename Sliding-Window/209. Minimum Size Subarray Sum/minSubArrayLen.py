class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        
        for i in range(len(nums)):
            if nums[i] >= target:
                return 1
        
        l = r = 0
        output = inf
        
        while r <= len(nums):
            current = sum(nums[l:r])
            if current >= target:
                l += 1
                current -= nums[l]
                output = min(output, r - l + 1)
            else:
                r += 1
        
        return output