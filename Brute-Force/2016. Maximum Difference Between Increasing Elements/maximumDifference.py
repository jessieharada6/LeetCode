class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        output = float('-inf')
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    output = max(output, nums[j] - nums[i])
        
        return output if output != float('-inf') else -1