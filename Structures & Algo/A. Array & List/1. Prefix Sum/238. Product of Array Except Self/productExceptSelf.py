class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1, 2, 3, 4]
        output = []
        base = 1
        for i in range(len(nums)):
            output.append(base)
            # base: 1, 1, 2, 6
            base *= nums[i]
        
        base = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= base
            # base: 24, 12, 4, 1
            base *= nums[i]
        
        return output